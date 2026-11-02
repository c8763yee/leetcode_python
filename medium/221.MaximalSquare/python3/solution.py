class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        max_side = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                    
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1])) + 1
                max_side = max(max_side, matrix[i][j])
                # if matrix[i][j] > max_side:
                #     max_side = matrix[i][j]

        return max_side ** 2
