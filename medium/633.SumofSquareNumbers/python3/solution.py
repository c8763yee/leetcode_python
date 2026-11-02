class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = 2 ** 16

        while left <= right:
            val = left * left + right * right
            if val == c:
                return True

            if val > c:
                right -= 1
            else:
                left += 1

        return False