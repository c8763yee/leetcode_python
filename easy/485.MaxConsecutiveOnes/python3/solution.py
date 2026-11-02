class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k=max_ = 0
        for i in nums:
            if i:
                k+=1
            else:
                k=0
            if k > max_: max_ = k 
        return max_