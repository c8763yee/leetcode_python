class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        dp = set()
        max_num = -1
        for i, e in enumerate(nums):
            if -e in dp:
                max_num = max(abs(e), max_num)
            dp.add(e)

        return max_num
