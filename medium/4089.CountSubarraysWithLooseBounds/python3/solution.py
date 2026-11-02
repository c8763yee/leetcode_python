class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        cnt = 0
        left = 0
        sum = 0
        for i, e in enumerate(nums):
            if not (minK <= e <= maxK):
                left = i+1
            else:
                cnt += i - left + 1
        return cnt
                
            
            
             