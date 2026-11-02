class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if dic.get(i, 0):
                return i
            
            else:
                dic[i]= 1