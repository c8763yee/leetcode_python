class Solution:
    def findDifference(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        return s1-s2, s2-s1
