class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = 0
        start = 0
        for i in range(k):
            max_sum += nums[i]
        curr_sum = max_sum
        for i in range(k, len(nums)):
            e = nums[i]
            curr_sum = curr_sum + e - nums[start]
            max_sum = max(max_sum, curr_sum)
            start += 1
        return round(max_sum/k, 5)