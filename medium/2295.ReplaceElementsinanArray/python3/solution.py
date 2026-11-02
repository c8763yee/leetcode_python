class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        size = len(nums)
        dp = nums[:]
        maps = {e: i for i, e in enumerate(nums)}
        for num, op in operations:
            num_index = maps.pop(num)
            nums[num_index] = dp[num_index] = op
            maps[op] = num_index

        return dp
