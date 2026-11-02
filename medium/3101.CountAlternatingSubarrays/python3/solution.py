class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        left = size = 0
        for right, e in enumerate(nums):
            if right != 0 and e == nums[right-1]:
                left = right
                
            size += (right - left + 1)
        return size