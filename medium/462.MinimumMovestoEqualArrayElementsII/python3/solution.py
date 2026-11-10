class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        cnt = 0
        mid = len(nums) // 2
        for i, e in enumerate(nums):
            if (i == mid): continue
            cnt += abs(nums[i] - nums[mid])
        return cnt
