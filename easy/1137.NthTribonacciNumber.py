class Solution:
    def __init__(self):
        self.dp = [0] * 38
        self.dp[1] = 1
        self.dp[2] = 1
    """
    iterative solution
    -------------------------
    def tribonacci(self, n):
        a,b,c,d = 0,1,1,2
        for _ in range(2, n):
            d = a+b+c
            a=b
            b=c
            c=d
        return d
    """
    def tribonacci(self, n):
        if n<3:
            return int(n>0)
        if not self.dp[n]:
            self.dp[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(
        return self.dp[n]
