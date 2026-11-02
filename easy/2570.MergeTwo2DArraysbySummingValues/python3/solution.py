class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = {}
        for i in (nums1, nums2):
            for k, v in i:
                if k in dic:
                    dic[k] += v
                    continue
                dic[k] = v
        return sorted(dic.items())