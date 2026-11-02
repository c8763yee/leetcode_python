class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row_size = len(mat)
        col_size = len(mat[0])

        checked = [(-1, -1) for _ in range(row_size*col_size+1)]
        row_count = [0 for _ in range(row_size)]
        col_count = [0 for _ in range(col_size)]

        for y in range(len(mat)):
            for x in range(len(mat[0])):
                checked[mat[y][x]] = (y, x)

        for i, e in enumerate(arr):
            y, x = checked[e]
            row_count[y] += 1
            col_count[x] += 1
            if row_count[y] == col_size or col_count[x] == row_size:
                return i

        
        return len(arr)-1
