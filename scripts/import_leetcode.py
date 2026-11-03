#!/usr/bin/env python3
"""Export this account's Accepted submissions without printing credentials."""
import argparse
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXTENSIONS = {'python3':'py','python':'py','c':'c','cpp':'cpp','java':'java','javascript':'js','typescript':'ts','csharp':'cs','golang':'go','rust':'rs','ruby':'rb','swift':'swift','kotlin':'kt','scala':'scala','php':'php','mysql':'sql','mssql':'sql','oraclesql':'sql','postgresql':'sql','bash':'sh','racket':'rkt','erlang':'erl','elixir':'ex','dart':'dart','pandas':'py','pythondata':'py'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--credentials', type=Path, default=ROOT / '.env.leetcode')
    parser.add_argument('--username', default='c8763yee')
    parser.add_argument('--resume', action='store_true', help='Reuse the previously downloaded history snapshot')
    args = parser.parse_args()
    values = {}
    credential_text = args.credentials.read_text() if args.credentials.exists() else ''
    for line in credential_text.splitlines():
        if '=' in line and not line.lstrip().startswith('#'):
            key, value = line.split('=', 1)
            values[key.strip()] = value.strip().strip('\"\'')
    for key in ('LEETCODE_SESSION', 'LEETCODE_CSRF_TOKEN'):
        if os.environ.get(key):
            values[key] = os.environ[key]
        if not values.get(key):
            raise SystemExit(f'Missing {key}: set the environment variable or provide {args.credentials.name}')
    headers = {'Content-Type':'application/json','Referer':'https://leetcode.com/','User-Agent':'Mozilla/5.0',
               'Cookie':'LEETCODE_SESSION='+values['LEETCODE_SESSION']+'; csrftoken='+values['LEETCODE_CSRF_TOKEN'],
               'x-csrftoken':values['LEETCODE_CSRF_TOKEN']}

    def query(document, variables=None):
        for attempt in range(5):
            try:
                request = urllib.request.Request('https://leetcode.com/graphql/', headers=headers,
                    data=json.dumps({'query':document,'variables':variables or {}}).encode())
                with urllib.request.urlopen(request, timeout=60) as response:
                    result = json.load(response)
                if result.get('errors'):
                    raise RuntimeError(str(result['errors']))
                return result['data']
            except (urllib.error.URLError, TimeoutError, RuntimeError):
                if attempt == 4:
                    raise
                time.sleep(2 ** attempt)

    user = query('query { userStatus { isSignedIn username } }')['userStatus']
    if not user['isSignedIn'] or user['username'] != args.username:
        raise RuntimeError('Authenticated account does not match requested username')
    cache = ROOT / '.leetcode-import' / args.username
    cache.mkdir(parents=True, exist_ok=True)
    if args.resume and (cache / 'history.json').exists():
        submissions = json.loads((cache / 'history.json').read_text())
    else:
        submissions = []
        offset = 0
        last_key = None
        while True:
            page = query('query($offset:Int!,$limit:Int!,$lastKey:String) { submissionList(offset:$offset,limit:$limit,lastKey:$lastKey) { hasNext lastKey submissions { id title titleSlug statusDisplay lang timestamp } } }',
                         {'offset':offset,'limit':100,'lastKey':last_key})['submissionList']
            rows = page['submissions']
            if page['hasNext'] and not rows:
                raise RuntimeError('Empty page before end of submission history')
            submissions.extend(rows)
            print(f'Listed {len(submissions)} submissions', flush=True)
            if not page['hasNext']:
                break
            offset += len(rows)
            last_key = page['lastKey']
            time.sleep(.2)
    if len({s['id'] for s in submissions}) != len(submissions):
        raise RuntimeError('Duplicate submission IDs: history may have changed; rerun')
    (cache / 'history.json').write_text(json.dumps(submissions, indent=2)+'\n')
    accepted = [s for s in submissions if s['statusDisplay'] == 'Accepted']
    accepted_count = len(accepted)
    latest_accepted = {}
    for sub in sorted(accepted, key=lambda row:(int(row['timestamp']),int(row['id'])), reverse=True):
        latest_accepted.setdefault((sub['titleSlug'],sub['lang']), sub)
    accepted = list(latest_accepted.values())
    print(f'Accepted submissions: {accepted_count}; latest problem/language solutions: {len(accepted)}', flush=True)
    details = {}
    pending = []
    for sub in accepted:
        file = cache / (sub['id']+'.json')
        if file.exists():
            details[sub['id']] = json.loads(file.read_text())
        else:
            pending.append(sub)
    newest_ids = {}
    for sub in sorted(accepted, key=lambda row:(int(row['timestamp']),int(row['id'])), reverse=True):
        newest_ids.setdefault((sub['titleSlug'], sub['lang']), sub['id'])
    priority = set(newest_ids.values())
    pending.sort(key=lambda sub: sub['id'] not in priority)
    fields = 'code statusCode timestamp lang { name } question { questionFrontendId title titleSlug difficulty }'
    for start in range(0, len(pending), 50):
        batch = pending[start:start+50]
        for attempt in range(12):
            document = 'query { ' + ' '.join('s'+sub['id']+': submissionDetails(submissionId:'+sub['id']+') { '+fields+' }' for sub in batch) + ' }'
            result = query(document)
            retry = []
            for sub in batch:
                detail = result.get('s'+sub['id'])
                if detail is None:
                    retry.append(sub)
                    continue
                if detail.get('statusCode') != 10 or not detail.get('code') or not detail.get('question'):
                    raise RuntimeError('Missing Accepted code or metadata for '+sub['id'])
                details[sub['id']] = detail
                (cache / (sub['id']+'.json')).write_text(json.dumps(detail)+'\n')
            if retry:
                print(f'Retrying {len(retry)} temporarily unavailable sources after cooldown', flush=True)
                time.sleep(55)
            else:
                time.sleep(2)
            batch = retry
            if not batch:
                break
        for sub in batch:
            details[sub['id']] = None
        print(f"Fetched {len(details)}/{len(accepted)} Accepted sources", flush=True)
    for sub in accepted:
        detail = details[sub['id']]
        if detail is None:
            continue
        if detail['lang']['name'] != sub['lang'] or detail['question']['titleSlug'] != sub['titleSlug']:
            raise RuntimeError('Submission metadata mismatch: '+sub['id'])
        if sub['lang'] not in EXTENSIONS:
            raise RuntimeError('Unknown language: '+sub['lang'])

    existing = {}
    for difficulty in ['easy','medium','hard']:
        for path in (ROOT / difficulty).iterdir():
            if path.is_dir() and '.' in path.name:
                key = path.name.split('.',1)[0]
                if key in existing:
                    raise RuntimeError('Duplicate existing problem directory: '+key)
                existing[key] = path
    unavailable = [sub for sub in accepted if details[sub['id']] is None]
    manifest = []
    latest = {}
    problems = {}
    for sub in accepted:
        detail = details[sub['id']]
        if detail is None:
            continue
        q = detail['question']
        qid = q['questionFrontendId']
        language = sub['lang']
        if not re.fullmatch(r'[a-z0-9]+', language):
            raise RuntimeError('Unsafe language directory')
        title = ''.join(re.findall(r'[A-Za-z0-9]+', q['title']))
        directory = existing.get(qid, ROOT / q['difficulty'].lower() / (qid+'.'+title))
        langdir = directory / language
        extension = EXTENSIONS[language]
        archive = langdir / ('solution.'+extension)
        archive.parent.mkdir(parents=True, exist_ok=True)
        code = detail['code']
        key = (qid,language)
        rank = (int(sub['timestamp']),int(sub['id']))
        if key not in latest or rank > latest[key][0]:
            latest[key] = (rank, langdir / ('solution.'+extension), code)
        problems[qid] = (q,directory)
        manifest.append({'id':sub['id'],'questionId':qid,'title':q['title'],'titleSlug':q['titleSlug'],
                         'difficulty':q['difficulty'],'language':language,'timestamp':int(sub['timestamp']),
                         'path':str(archive.relative_to(ROOT)),'sha256':hashlib.sha256(code.encode()).hexdigest()})
    backups = 0
    for rank, file, code in latest.values():
        if file.exists() and file.read_text() != code:
            old = file.read_bytes()
            backup = cache / 'previous-local' / file.relative_to(ROOT)
            backup.parent.mkdir(parents=True,exist_ok=True)
            if not backup.exists():
                backup.write_bytes(old)
            backups += 1
        file.write_text(code)
    report = {'username':args.username,'totalSubmissions':len(submissions),'acceptedSubmissions':accepted_count,
              'problems':len(problems),'problemLanguages':len(latest),'unavailable':unavailable,'submissions':manifest}
    (ROOT / 'submissions.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    readme = ROOT / 'README.md'
    intro = readme.read_text().split('| id',1)[0].split('程式碼依 `',1)[0]
    intro += '程式碼依 `難度/題號.題名/語言/solution.副檔名` 分類；`solution` 為該語言最新的 Accepted 提交，每題各語言僅保留最新 Accepted，提交 ID、時間與程式碼雜湊見 [submissions.json](submissions.json)。\n\n'
    intro += '重新同步：`python3 scripts/import_leetcode.py`（從 `.env.leetcode` 讀取登入 Cookie）；下載中斷時可加 `--resume`，沿用上次的歷史清單與快取。本機舊解答備份於 `.leetcode-import/c8763yee/previous-local/`。\n\n'
    intro += '每日自動同步與 Discord 失敗通知設定：[自動化說明](docs/automation.md)。\n\n'
    intro += '| id | Difficulty | Title | Languages |\n|---|---|---|---|\n'
    for qid,(q,directory) in sorted(problems.items(),key=lambda item:(not item[0].isdigit(),int(item[0]) if item[0].isdigit() else item[0])):
        links = []
        for (pid,lang),(_,file,_) in sorted(latest.items()):
            if pid == qid:
                links.append(f'[{lang}]({file.relative_to(ROOT)})')
        intro += f"| {qid} | {q['difficulty']} | [{q['title']}]({directory.relative_to(ROOT)}) | {', '.join(links)} |\n"
    readme.write_text(intro)
    print(json.dumps({k:v for k,v in report.items() if k not in ('submissions','unavailable')}),flush=True)
    print(f'Previous local solutions backed up: {backups} (under .leetcode-import/{args.username}/previous-local)',flush=True)
    if unavailable:
        raise SystemExit(f'Incomplete: {len(unavailable)} sources unavailable; see submissions.json and retry --resume')

if __name__ == '__main__':
    main()
