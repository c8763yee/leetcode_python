# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def node_height(node):
            if node is None:
                return 0, True

            left_height, left_balanced = node_height(node.left)
            right_height, right_balanced = node_height(node.right)
            if (not (left_balanced and right_balanced)
                or abs(left_height - right_height) > 1
                ):
                return -1, False

            return max(left_height, right_height) + 1, True

        height, is_balanced = node_height(root)
        return is_balanced

