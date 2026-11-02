class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        zeros = 0
        max_length = 0
        for current_index, e in enumerate(nums):
            if e == 0:
                zeros += 1
            if zeros > k:
                max_length = max(max_length, current_index - start)
                while zeros > k and start <= current_index:
                    zeros -= (nums[start] == 0)
                    start += 1

        return max(max_length, len(nums)-start)
    def longestSubarray(self, nums: List[int]) -> int:
        return self.longestOnes(nums, 1) - 1