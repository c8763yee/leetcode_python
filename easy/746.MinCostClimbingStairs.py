class Solution:
    def minCostClimbingStairs(self, cost):
        cost.append(0)
        n = len(cost)
        for i in range(n-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[:2])
