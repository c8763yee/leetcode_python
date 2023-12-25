#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#


# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ones = 0
        for zeros in range(len(nums)):
            if nums[zeros] != 0:
                nums[zeros], nums[ones] = nums[ones], nums[zeros]
                ones += 1


# @lc code=end
