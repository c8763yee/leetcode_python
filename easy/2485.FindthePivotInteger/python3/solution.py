class Solution:
    def pivotInteger(self, n: int) -> int:
        right_sum = (n+1)*n//2
        left_sum = 0
        for left in range(1, n+1):
            left_sum += left
            if left_sum == right_sum:
                return left
            right_sum -= left

        return -1
        