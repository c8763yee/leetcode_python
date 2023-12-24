#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (52.97%)
# Likes:    9022
# Dislikes: 909
# Total Accepted:    1.3M
# Total Submissions: 2.5M
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings a and b, return their sum as a binary string.
#
#
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
#
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
#
#
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        # Intuition:
        first, check if either a or b is 0, if so, return the other string
        then iterate through both string backwards, calculate the sum of the two digits and the carry bit 
            until both strings are indexed out and there is no carry bit left

        Args:
            a (str): _description_
            b (str): _description_

        Returns:
            str: _description_
        """
        index_a = len(a) - 1
        index_b = len(b) - 1
        if a == '0' or b == '0':
            return a if a != '0' else b

        binary_list = []
        carry = val = 0
        while index_a >= 0 or index_b >= 0 or carry:
            val = (
                ord(a[index_a] if index_a >= 0 else '0') +
                ord(b[index_b] if index_b >= 0 else '0') +
                carry - 2 * ord('0')
            )

            carry = val >> 1
            binary_list.append(val % 2)
            index_a -= 1
            index_b -= 1
        return ''.join(map(str, binary_list[::-1]))


# @lc code=end
