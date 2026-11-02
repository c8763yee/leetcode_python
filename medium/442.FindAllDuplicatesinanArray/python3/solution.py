class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
                continue
            dic[i]=1
        return [i for i in dic if dic[i]>1]