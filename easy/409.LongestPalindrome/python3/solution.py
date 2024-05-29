#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (53.90%)
# Likes:    5169
# Dislikes: 342
# Total Accepted:    585.1K
# Total Submissions: 1.1M
# Testcase Example:  '"abccccdd"'
#
# Given a string s which consists of lowercase or uppercase letters, return the
# length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome
# here.
#
#
# Example 1:
#
#
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose
# length is 7.
#
#
# Example 2:
#
#
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is
# 1.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.
#
#
#

# @lc code=start
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        # Intuition:
            count all occurences of each character, then add up all even counts
            if there is any odd count, add 1 to the result.
        # complexity:
            $O(n)$ T.C , because we need to iterate through the string once and count the occurences
            $O(n)$ S.C, because we need to create a hashmap to store the occurences of each character

        Args:
            s (str): _description_

        Returns:
            int: _description_
        """
        total = 0
        is_odd = False
        for v in Counter(s).values():
            if v == 1:
                is_odd = True
            else:
                total += v // 2
                is_odd = is_odd or v % 2 == 1

        return total * 2 + is_odd
# @lc code=end
