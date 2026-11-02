class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for idx in range(len(nums)):            
            right_sum -= nums[idx]
            if left_sum == right_sum:
                return idx
            left_sum += nums[idx]

        return -1