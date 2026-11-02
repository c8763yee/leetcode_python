class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # dp[0][i]: minimum element in row i
        # dp[1][j]: maximum element in column j
        m = len(matrix)
        n = len(matrix[0])

        min_row = [float('inf') for _ in range(m)]
        max_col =  [0 for _ in range(n)]
        for i, row in enumerate(matrix):
            for j, ele in enumerate(row):
                min_row[i] = ele if ele < min_row[i] else min_row[i]
                max_col[j] = ele if ele > max_col[j] else max_col[j]

        return [matrix[i][j] for j in range(n) for i in range(m) if min_row[i] == max_col[j]]