#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (51.02%)
# Likes:    10205
# Dislikes: 608
# Total Accepted:    1.3M
# Total Submissions: 2.6M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
#
# Example 3:
#
#
# Input: root = []
# Output: true
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_node_height(node):
            if node is None:
                return 0, True

            left_height, left_balanced = get_node_height(node.left)
            right_height, right_balanced = get_node_height(node.right)
            if (not (left_balanced and right_balanced)
                    or abs(left_height - right_height) > 1):

                return -1, False

            return max(left_height, right_height) + 1, True

        height, is_balanced = get_node_height(root)
        return is_balanced


# @lc code=end
