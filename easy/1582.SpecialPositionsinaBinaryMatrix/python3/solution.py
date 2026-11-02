class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # O(NM) time
        # O(max(N,M)) space
        row = len(mat)
        col = len(mat[0])
        ones = [[0 for _ in range(max(row, col))] for _ in range(2)]

        special = 0
        for i in range(row):
            for j in range(col):
                ones[0][i] += (mat[i][j] == 1)
                ones[1][j] += (mat[i][j] == 1)

        for i in range(row):
            for j in range(col):
                if not mat[i][j]:
                    continue
                special += (ones[0][i] == ones[1][j] and ones[1][j] == 1)
        return special