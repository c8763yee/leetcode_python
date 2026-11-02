class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size = len(mat)
        return sum(mat[i][i]+mat[i][size-i-1] for i in range(size)) - mat[size//2][size//2] * (size%2)