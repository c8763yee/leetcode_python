import contextlib
import importlib.util
import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    'import_leetcode', Path(__file__).resolve().parents[1] / 'scripts/import_leetcode.py'
)
importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(importer)


class ImportAutomationTests(unittest.TestCase):
    def test_environment_credentials_and_latest_per_language(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for difficulty in ('easy', 'medium', 'hard'):
                (root / difficulty).mkdir()
            (root / 'README.md').write_text('# Solutions\n')
            credentials = root / 'cookies'
            credentials.write_text('LEETCODE_SESSION=old-session\nLEETCODE_CSRF_TOKEN=old-csrf\n')
            rows = [
                {'id': str(i), 'title': 'Two Sum', 'titleSlug': 'two-sum',
                 'statusDisplay': status, 'lang': lang, 'timestamp': str(i)}
                for i, status, lang in [(4, 'Wrong Answer', 'c'), (3, 'Accepted', 'c'),
                                        (2, 'Accepted', 'python3'), (1, 'Accepted', 'python3')]
            ]
            requested = []

            def respond(request, timeout):
                self.assertEqual(request.get_header('Cookie'),
                                 'LEETCODE_SESSION=new-session; csrftoken=new-csrf')
                self.assertEqual(request.get_header('X-csrftoken'), 'new-csrf')
                document = json.loads(request.data)['query']
                requested.append(document)
                if 'userStatus' in document:
                    data = {'userStatus': {'isSignedIn': True, 'username': 'c8763yee'}}
                elif 'submissionList' in document:
                    data = {'submissionList': {'hasNext': False, 'lastKey': None, 'submissions': rows}}
                else:
                    self.assertNotIn('submissionId:1)', document)
                    self.assertNotIn('submissionId:4)', document)
                    data = {
                        's' + str(i): {'code': code, 'statusCode': 10, 'timestamp': i,
                                      'lang': {'name': lang},
                                      'question': {'questionFrontendId': '1', 'title': 'Two Sum',
                                                   'titleSlug': 'two-sum', 'difficulty': 'Easy'}}
                        for i, lang, code in [(2, 'python3', 'python source\n'), (3, 'c', 'C source\n')]
                    }
                return io.BytesIO(json.dumps({'data': data}).encode())

            with patch.object(importer, 'ROOT', root), patch.dict(os.environ, {
                'LEETCODE_SESSION': 'new-session', 'LEETCODE_CSRF_TOKEN': 'new-csrf'
            }, clear=True), patch('sys.argv', ['import', '--credentials', str(credentials)]), \
                    patch.object(importer.urllib.request, 'urlopen', side_effect=respond), \
                    patch.object(importer.time, 'sleep'), contextlib.redirect_stdout(io.StringIO()):
                importer.main()
            self.assertEqual(len(requested), 3)
            report = json.loads((root / 'submissions.json').read_text())
            self.assertEqual(report['acceptedSubmissions'], 3)
            self.assertEqual({s['id'] for s in report['submissions']}, {'2', '3'})
            self.assertEqual((root / 'easy/1.TwoSum/c/solution.c').read_text(), 'C source\n')
            self.assertIn('docs/automation.md', (root / 'README.md').read_text())

    def test_missing_secrets_fail_before_network(self):
        with tempfile.TemporaryDirectory() as temporary:
            absent = str(Path(temporary) / 'missing')
            with patch.dict(os.environ, {}, clear=True), \
                    patch('sys.argv', ['import', '--credentials', absent]), \
                    patch.object(importer.urllib.request, 'urlopen') as network:
                with self.assertRaisesRegex(SystemExit, 'Missing LEETCODE_SESSION'):
                    importer.main()
                network.assert_not_called()

    def test_mismatched_account_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            response = io.BytesIO(json.dumps({'data': {'userStatus': {
                'isSignedIn': True, 'username': 'someone-else'
            }}}).encode())
            with patch.object(importer, 'ROOT', root), \
                    patch.dict(os.environ, {'LEETCODE_SESSION': 'session', 'LEETCODE_CSRF_TOKEN': 'csrf'}, clear=True), \
                    patch('sys.argv', ['import', '--credentials', str(root / 'missing')]), \
                    patch.object(importer.urllib.request, 'urlopen', return_value=response):
                with self.assertRaisesRegex(RuntimeError, 'does not match'):
                    importer.main()
            self.assertEqual(list(root.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
