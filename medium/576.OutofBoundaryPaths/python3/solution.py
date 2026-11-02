class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[-1 for _ in range(maxMove+1)] for _ in range(n)] for _ in range(m)]
        def f(i, j, max_move):
            if not (0 <= i < m and 0 <= j < n):
                return 1
            
            if max_move <= 0:
                return 0

            if dp[i][j][max_move] == -1:
                dp[i][j][max_move] = (
                    f(i+1, j, max_move-1) + 
                    f(i, j+1, max_move-1) + 
                    f(i-1, j, max_move-1) + 
                    f(i, j-1, max_move-1)
                ) % (10**9+7)

            return dp[i][j][max_move]
        return f(startRow, startColumn, maxMove)
            

            