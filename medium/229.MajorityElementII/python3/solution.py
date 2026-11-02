class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        table = {}
        for i in nums:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        return [i for i, v in table.items() if v > len(nums)//3]