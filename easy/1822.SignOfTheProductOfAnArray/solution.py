class Solution:
    def arraySign(self, nums):
        cnt = True
        for n in nums:
            if n== 0:
                return 0
            cnt ^= n<0
        if cnt:
            return 1
        return -1
