MAX_INT = (2 << 31) - 1


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [MAX_INT for _ in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            cost = costs[i-1]
            if i>=1:
                jump_cost = cost + 1
                dp[i] = min(dp[i], dp[i-1]+jump_cost)
            if i>=2:
                jump_cost = cost + 4
                dp[i] = min(dp[i], dp[i-2]+jump_cost)
            if i>=3:
                jump_cost = cost + 9
                dp[i] = min(dp[i], dp[i-3]+jump_cost)

        return dp[n]