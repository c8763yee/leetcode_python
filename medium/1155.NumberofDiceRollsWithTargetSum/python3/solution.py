class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:    

        # f(n, target) = \sum_i=1^k f(n-1, target-i)
        # f(0, k, 0) = 1
        dp= [[-1 for i in range(target + 1)] for _ in range(n + 1)]

        def f(d, t): # find possible ways to roll `n` dices with `k` faces to point `t`
            if t<0:
                return 0
            if d == 0:
                return t == 0
            if dp[d][t] != -1:
                return dp[d][t]
            
            sum_val = 0
            for i in range(1, k+1):
                sum_val += f(d-1, t-i)
            dp[d][t] = sum_val % (10**9+7)
            return dp[d][t]
        
        
        return f(n, target) 
            

