# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, val):
            if node is None:
                return False
            if node.left or node.right:
                return dfs(node.left, val - node.val) or dfs(node.right, val - node.val)
            return val == node.val
        return dfs(root, targetSum)
            