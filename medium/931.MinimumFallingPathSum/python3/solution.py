class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row_size = len(matrix)
        col_size = len(matrix[0])
        for i in range(1, row_size):
            for j in range(col_size):
                diff = matrix[i-1][j]
                if 0 < j:
                    diff = min(diff, matrix[i-1][j-1])

                if j+1 < col_size:
                    diff = min(diff, matrix[i-1][j+1])

                matrix[i][j] += diff

        return min(matrix[-1])                
