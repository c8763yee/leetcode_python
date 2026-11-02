class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        for i, num in enumerate(nums):
            if i == 0:
                continue
            for j in range(i):
                if num > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)