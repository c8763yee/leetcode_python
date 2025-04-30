from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(
            i == 0 or 10 <= i < 100 or 1000 <= i < 10000 or i == 100000 for i in nums
        )
