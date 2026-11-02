class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        left = top = float('-inf')
        right = bottom = float('inf')
        for i, row in enumerate(grid):
            for j, ele in enumerate(row):
                if ele == 0:
                    continue
                    
                top = max(top, i)
                bottom = min(bottom, i)
                left = max(left, j)
                right = min(right, j)

        return (top-bottom+1)*(left-right+1)