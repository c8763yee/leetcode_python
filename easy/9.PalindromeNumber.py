class Solution:
    def isPalindrome(self, x):
        if x <= 0:
            return x == 0
        tmp = x
        val = 0
        while tmp:
            val = val*10 + tmp%10
            tmp //= 10
        return val == x
