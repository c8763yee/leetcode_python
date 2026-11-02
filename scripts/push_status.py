#!/usr/bin/env python3
"""Print local problem count / LeetCode's current solved count for commits."""
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUERY = '''query { matchedUser(username: "c8763yee") {
    submitStatsGlobal { acSubmissionNum { difficulty count } }
} }'''


def main():
    request = urllib.request.Request(
        'https://leetcode.com/graphql/',
        data=json.dumps({'query': QUERY}).encode(),
        headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)
    if result.get('errors'):
        raise ValueError('LeetCode returned GraphQL errors')
    user = result['data']['matchedUser']
    counts = user['submitStatsGlobal']['acSubmissionNum']
    total = next(row['count'] for row in counts if row['difficulty'] == 'All')
    if type(total) is not int or total < 0:
        raise ValueError('LeetCode returned an invalid solved count')
    local = sum(
        1
        for difficulty in ('easy', 'medium', 'hard')
        for problem in (ROOT / difficulty).iterdir()
        if problem.is_dir() and any(problem.glob('*/solution.*'))
    )
    print(f'{local}/{total}')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError, StopIteration) as error:
        print(f'Cannot determine push status: {error}', file=sys.stderr)
        sys.exit(1)
