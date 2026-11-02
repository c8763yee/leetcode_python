MAX_INT = 2 ** 31 - 1

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        size: int = len(grid[0])
        dp: list[list[int]] = [[MAX_INT for _ in range(size)] for _ in range(size)]
        def run(r: int, c: int, size: int):
            if r == size - 1:
                dp[r][c] = grid[r][c]
                
            elif dp[r][c] == MAX_INT:
                dp[r][c] = min((run(r+1, i, size) + grid[r][c]) for i in range(size) if i != c)
            return dp[r][c]

        return min(map(lambda i: run(0, i, size), range(size)))