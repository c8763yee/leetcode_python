# [0,1,1,2,3,5]
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        for i in range(n):
           c = a+b
           a = b
           b = c
        return b