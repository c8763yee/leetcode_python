class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        m = {}
        for i, n in enumerate(s):
            if n not in m:
                m[n]=i
        return map(lambda k:m[k], nums)