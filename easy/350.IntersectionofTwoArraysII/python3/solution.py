class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        arr = []
        m, n = map(len,[nums1, nums2])
        i = j = 0
        while i<m and j<n:
            if nums1[i] == nums2[j]:
                arr.append(nums1[i])
                i+=1
                j +=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return arr