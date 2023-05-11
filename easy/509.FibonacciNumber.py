class Solution:
    def __init__(self, n):
        self.dp = [0] * 31
        self.dp[1] = 1
    def fib(self, n):
        """
        iterative solution
        ------------------------
        if n <= 1:
            return n
        a,b,c = 0,1,1
        for _ in range(2, n+1):
            c = a+b
            a = b
            b = c
        return c
        """
        if n <= 1:
            return int(n==1)
        if not self.dp[n]:
            self.dp[n] = self.fib(n-1)+self.fib(n-2)
        return self.dp[n]
