class Solution:
    def rob(self, nums):
        def robbing(idx, size):
            if idx >= size:
                return 0
            if dp[idx] == -1:
                dp[idx] = max(
                            robbing(idx+2, size) + nums[idx],
                            robbing(idx+1, size)
                        )
                return dp[idx]
        dp = [-1 for _ in nums]
        return robbing(0, len(nums))
