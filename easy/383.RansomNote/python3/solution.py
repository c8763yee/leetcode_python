#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (60.19%)
# Likes:    4705
# Dislikes: 479
# Total Accepted:    983.1K
# Total Submissions: 1.6M
# Testcase Example:  '"a"\n"b"'
#
# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#
# Constraints:
#
#
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
#
#
#

# @lc code=start
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """this problem can be reduced to a problem of check if ransomNote is a subset of magazine

        Args:
            ransomNote (str): _description_
            magazine (str): _description_

        Returns:
            bool: _description_
        """
        return not Counter(ransomNote) - Counter(magazine)
# @lc code=end
