class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = - n

        if x == 0:
            return 0
        if x == 1 or n == 0:
            return 1
        if n == 1:
            return x

        return self.myPow(x*x, n >> 1) * (x*(n & 1) or 1)