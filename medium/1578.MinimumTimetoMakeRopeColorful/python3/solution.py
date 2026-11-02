class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_cost = 0
        max_cost = 0
        current_cost = 0

        for i, e in enumerate(colors):
            if i > 0 and e != colors[i - 1]:
                total_cost += current_cost - max_cost
                current_cost = 0
                max_cost = 0

            current_cost += neededTime[i]
            max_cost = max(max_cost, neededTime[i])

        total_cost += current_cost - max_cost

        return total_cost
