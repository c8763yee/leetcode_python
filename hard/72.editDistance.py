class Solution:
    def minDistance(self, word1, word2):
        if word1 == word2:
            return 0
        alpha = 1 # insertion
        beta = 2 # deletion
        gamma = -1 # replace
        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        A = dp.copy()
        if not m or n:
            return max(m, n)

        for i in range(m+1):
            A[i][0] = i*beta
            dp[i][0] = i
        for j in range(n+1):
            A[0][j] = j*alpha
            dp[0][j] = j
        
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    A[i+1][j+1] = A[i][j]
                    dp[i+1][j+1] = dp[i][j]
                else:
                    A[i+1][j+1] = min(
                                A[i+1][j]+alpha,
                                A[i][j+1]+beta,
                                A[i][j]+gamma
                            )
                    dp[i+1][j+1] = 1 + min(
                                dp[i+1][j],
                                dp[i][j+1],
                                dp[i][j]
                            )
        return op[-1][-1]
