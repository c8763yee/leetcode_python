class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        sum_val = sum(i*(1-j) for i, j in zip(customers, grumpy))
        diff = 0
        
        for i in range(minutes):
            if grumpy[i] == 0:
                continue

            diff += customers[i]
        max_val = diff + sum_val
        diff -= customers[0] * grumpy[0]
        for i in range(1, len(customers)-minutes+1):
            diff += customers[i+minutes-1] * grumpy[i+minutes-1]
            max_val = max(max_val, diff+sum_val)
            diff -= customers[i] * grumpy[i]
        return max_val