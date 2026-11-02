class Solution:
    def minCostClimbingStairs(self, cost):
        dp = [-1 for _ in cost]
        def dfs(size, index=0):
            if index >= size:
                return 0
            if dp[index] == -1:
                dp[index] = cost[index] + min(
                    dfs(size, index+1),
                    dfs(size, index+2),
                )
            return dp[index]
        return min(dfs(len(cost)), dfs(len(cost), 1))