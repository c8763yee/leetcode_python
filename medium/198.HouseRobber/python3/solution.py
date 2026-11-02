class Solution:
    def rob(self, nums: List[int]) -> int:
        a = b = 0
        for i in nums:
            a, b = max(b+i, a), a

        return a
