class Solution:
    def twoSum(self, nums, target):
        table = {}
        for i, e in enumerate(nums):
            if target-e in table:
                return [table[target-e], i]
            table[e] = i
