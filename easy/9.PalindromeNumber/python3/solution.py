#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (55.09%)
# Likes:    11750
# Dislikes: 2643
# Total Accepted:    4M
# Total Submissions: 7.3M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
#
#
# Example 1:
#
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
#
# Example 2:
#
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a
# palindrome.
#
#
#
# Constraints:
#
#
# -2^31 <= x <= 2^31 - 1
#
#
#
# Follow up: Could you solve it without converting the integer to a string?
#


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <= 9:
            return x >= 0
        num = 0
        y = x
        while y:
            num = num * 10 + y % 10
            y //= 10
        return x == num


# @lc code=end
