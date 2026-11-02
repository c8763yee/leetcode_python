class Solution:
    def arraySign(self, nums):
        cnt = True
        for n in nums:
            if not n:
                return 0
            cnt ^= n<0
        if cnt:
            return 1
        return -1