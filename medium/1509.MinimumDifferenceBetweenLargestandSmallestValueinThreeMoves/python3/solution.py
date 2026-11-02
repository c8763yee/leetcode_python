class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # Just convert entire list to 0 if size <= 3 
        if len(nums) <= 4:
            return 0

        nums.sort()
        return min(
            abs(nums[-4+i] - nums[i]) for i in range(4)
        )