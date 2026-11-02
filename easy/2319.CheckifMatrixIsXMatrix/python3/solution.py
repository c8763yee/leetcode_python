class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        length = len(grid)
        for r in range(length):
            for c in range(length):
                x = grid[r][c]
                if (r==c or length == r+c+1): 
                    if not x:
                        return False
                elif x:
                    return False
        return True
