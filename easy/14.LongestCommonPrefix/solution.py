#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (41.99%)
# Likes:    16560
# Dislikes: 4352
# Total Accepted:    2.9M
# Total Submissions: 7M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
#
# Example 1:
#
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
#
# Constraints:
#
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
#
#
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        # loop and insert (c in word) into trie
        for c in word:
            # if c is not next character then insert c into trie
            if c not in node.children:
                node.children[c] = TrieNode()
            # move to next node
            node = node.children[c]
        # set last node as end of word
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            # c not in word
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.insert(word)

        prefix = ''
        node = trie.root
        while node and node.is_end is False and len(node.children) == 1:
            prefix += next(iter(node.children.keys()))
            node = node.children[prefix[-1]]

        return prefix

# @lc code=end
