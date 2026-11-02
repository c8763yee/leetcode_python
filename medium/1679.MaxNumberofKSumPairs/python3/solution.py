class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        start = 0
        end = len(nums) - 1
        count = 0
        nums.sort()
        while start < end:
            sum_val = nums[start] + nums[end]
            if sum_val == k:
                count += 1
            if sum_val <= k:
                start += 1
            if sum_val >= k:
                end -= 1

        return count