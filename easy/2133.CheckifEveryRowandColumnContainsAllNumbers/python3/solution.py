class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        size = len(matrix)
        for m in matrix:
            if set(range(1, size+1)) - set(m):
                return False

        for i in range(size):
            sets = set()
            for j in range(size):
                if matrix[j][i] in sets:
                    return False
                sets.add(matrix[j][i])
        
        return True