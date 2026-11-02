class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        num = 0
        nums.sort()
        for i, e in enumerate(nums):
            if i%2==0:
                num += e

        return num