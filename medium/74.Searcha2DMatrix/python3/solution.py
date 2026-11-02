class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(left, right, target, c):
            if left > right:
                return False
            mid = (left + right) // 2
            midVal = matrix[mid//c][mid%c]
            if midVal == target:
                return True
            if midVal < target:
                return bs(mid+1, right, target,c)
            return bs(left, mid - 1, target, c)
        return bs(0, len(matrix)*len(matrix[0])-1, target, len(matrix[0]))