class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        zeros = 0
        max_length = 0
        for i, e in enumerate(nums):
            if e == 0:
                zeros += 1
            if zeros > k:
                max_length = max(max_length, i - start)
                while zeros > k and start <= i:
                    zeros -= (nums[start] == 0)
                    start += 1

        return max(max_length, len(nums)-start)
