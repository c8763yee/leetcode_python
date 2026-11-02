class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(grid):
            for j, ele in enumerate(row):
                if i == j == 0:
                    continue
                
                elif i == 0:
                    grid[i][j] += grid[i][j-1]

                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]