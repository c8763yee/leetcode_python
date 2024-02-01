#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#
# https://leetcode.com/problems/backspace-string-compare/description/
#
# algorithms
# Easy (49.08%)
# Likes:    7356
# Dislikes: 340
# Total Accepted:    774.8K
# Total Submissions: 1.6M
# Testcase Example:  '"ab#c"\n"ad#c"'
#
# Given two strings s and t, return true if they are equal when both are typed
# into empty text editors. '#' means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.
#
#
# Example 1:
#
#
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
#
#
# Example 2:
#
#
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
#
#
# Example 3:
#
#
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
#
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
#
#
#
# Follow up: Can you solve it in O(n) time and O(1) space?
#
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for c in s:
            if c == '#' and stack_s:
                stack_s.pop()
            elif c != '#':
                stack_s.append(c)

        for c in t:
            if c == '#' and stack_t:
                stack_t.pop()
            elif c != '#':
                stack_t.append(c)

        return stack_s == stack_t

# @lc code=end
