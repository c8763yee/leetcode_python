#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.61%)
# Likes:    10073
# Dislikes: 533
# Total Accepted:    1.1M
# Total Submissions: 2.5M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an integer array nums of length n and an integer target, find three
# integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
#
#
# Example 1:
#
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#
# Example 2:
#
#
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
#
#
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        current_val = float('inf')
        for pivot, pivot_val in enumerate(nums):
            start = pivot + 1
            end = len(nums) - 1
            while start < end:
                sum_val = pivot_val + nums[start] + nums[end]
                if sum_val == target:
                    return sum_val

                if sum_val > target:
                    end -= 1
                else:
                    start += 1

                if abs(target - sum_val) < closest:
                    closest = abs(target - sum_val)
                    current_val = sum_val

        return current_val

# @lc code=end
