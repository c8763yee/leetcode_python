#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (63.87%)
# Likes:    17741
# Dislikes: 540
# Total Accepted:    2.3M
# Total Submissions: 3.6M
# Testcase Example:  '[3,2,3]'
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You
# may assume that the majority element always exists in the array.
#
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#

# @lc code=start
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        # Intuition:
        since the majority element appears more than n/2 times, it will be the most common element in the list

        Args:
            nums (List[int]): _description_

        Returns:
            int: _description_
        """
        return Counter(nums).most_common(1)[0][0]
# @lc code=end
