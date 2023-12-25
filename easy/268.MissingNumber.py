#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (64.59%)
# Likes:    11102
# Dislikes: 3260
# Total Accepted:    1.8M
# Total Submissions: 2.8M
# Testcase Example:  '[3,0,1]'
#
# Given an array nums containing n distinct numbers in the range [0, n], return
# the only number in the range that is missing from the array.
#
#
# Example 1:
#
#
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range
# [0,3]. 2 is the missing number in the range since it does not appear in
# nums.
#
#
# Example 2:
#
#
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range
# [0,2]. 2 is the missing number in the range since it does not appear in
# nums.
#
#
# Example 3:
#
#
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range
# [0,9]. 8 is the missing number in the range since it does not appear in
# nums.
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^4
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
#
#
#
# Follow up: Could you implement a solution using only O(1) extra space
# complexity and O(n) runtime complexity?
#
#


# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """

        # Intuition
        <!-- Describe your first thoughts on how to solve this problem. -->
        My first thoughts is use a `set()` to store 0~n, then iterate through all elements in `nums` and check if the element is in sets. If the element in the sets then discard it from sets, otherwise it's the missing number.

        After saw follow-up question, I think we can use the sum of 0~n minus the sum of `nums` to get the missing number instead.
        since sum of `nums` if equals to sum of 0~n minus the missing number
        # Approach
        <!-- Describe your approach to solving the problem. -->
        1. since sum of nums is equals to sum of 0 to n and minus the missing number
        we can first calculate the sum of 0 to n and minus the sum of `nums` to get the missing number
        # Complexity
        - Time complexity:
        <!-- Add your time complexity here, e.g. $$O(n)$$ -->
        O(n), since we need to iterate through all elements in `nums` to get the sum of `nums`
        - Space complexity:
        <!-- Add your space complexity here, e.g. $$O(n)$$ -->
        O(1), since we only need to store the sum of 0 to n and the sum of `nums`
        """
        n = len(nums)
        size = n * (n + 1) // 2
        return size - sum(nums)


# @lc code=end
