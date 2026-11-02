class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def swap(a, b):
            return b, a
        n = len(matrix)
        for i in range(n//2):
            matrix[i], matrix[n-i-1] = swap(matrix[i], matrix[n-i-1])
        
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = swap(matrix[i][j], matrix[j][i])