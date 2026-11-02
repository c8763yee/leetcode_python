class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <= 9:
            return x >= 0
        num = 0
        y = x
        while y:
            num = num * 10 + y % 10
            y //= 10
        return x == num

