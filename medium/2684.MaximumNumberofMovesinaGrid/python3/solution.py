class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        # Process columns from right to left
        for col in range(n - 2, -1, -1):
            for row in range(m):
                for move in (-1, 0, 1):
                    new_row = row + move
                    if 0 <= new_row < m and grid[new_row][col + 1] > grid[row][col]:
                        dp[row][col] = max(dp[row][col], 1 + dp[new_row][col + 1])
        
        # Find the maximum number of moves starting from any cell in the first column
        max_moves = max(dp[row][0] for row in range(m))
        return max_moves
