from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(i % 100 >= 10 or i % 100000 == 0 for i in nums)
