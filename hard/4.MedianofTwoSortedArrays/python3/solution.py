class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        size = len(nums)
        
        if size %2:
            return nums[size//2]
        else:
            return (nums[size//2] + nums[size//2-1]) / 2