class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # if a[i] and b[j] are same, set table[i][j] to 1
                # and find in i-1, j-1
                # otherwise set table[i][j] by maximum of size in same (row/column) 
        val = 0
        for i in range(m):
            if text1[i] == text2[0]:
                val = 1
            dp[i][0] =val

        val = 0
        for i in range(n):
            if text2[i] == text1[0]:
                val = 1
            dp[0][i] =val

        for i in range(1, m):
            for j in range(1, n):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        # def walk(i, j):
        #     if i < 0 or j < 0:
        #         return 0 
        #     if dp[i][j] == 0:
                
        #         if text1[i] == text2[j]:
        #             dp[i][j] = walk(i-1, j-1) + 1
        #         else:
        #             dp[i][j] = max(walk(i-1, j), walk(i, j-1))
        #     return dp[i][j]
        return dp[m-1][n-1]