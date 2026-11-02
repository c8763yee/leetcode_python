class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        psr=ngr=0
        for i in nums:
            if i == 0:
                continue
            if i<0:ngr += 1
            else: psr+=1
        if psr<ngr:  return ngr
        return psr