class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        people = len(languages)
        nocommon = [False for _ in range(people)]

        should_return = True
        for u, v in friendships:
            if set(languages[u-1]).intersection(languages[v-1]) == set():
                nocommon[u-1] = nocommon[v-1] = True
                should_return = False

        if should_return:
            return 0

        # print(nocommon)

        dp = [[0]*n for _ in range(people)]
        for i in range(people):
            if nocommon[i] is False:
                continue

            for j in languages[i]:
                dp[i][j-1] = 1

        # print(*dp, sep='\n')
        
        max_learned = 0
        for lang in range(n):
            learned = 0
            for cur in range(people):
                learned += dp[cur][lang] or nocommon[cur] is False

            max_learned = max(learned, max_learned)

        return people - max_learned