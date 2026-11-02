class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set(nums)
        max_num = 1
        for i in s:
            num = 1
            while i*i in s:
                num += 1
                i *= i

            max_num = max(max_num, num)

        return max_num if max_num != 1 else -1