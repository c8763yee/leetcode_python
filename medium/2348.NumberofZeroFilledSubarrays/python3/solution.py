class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = total = 0        
        for i in nums:
            if i:
                cnt = 0
                continue
            cnt += 1
            total += cnt
        return total