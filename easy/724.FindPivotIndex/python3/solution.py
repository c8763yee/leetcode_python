class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for idx, e in enumerate(nums):            
            right_sum -= e
            if left_sum == right_sum:
                return idx
            left_sum += e

        return -1