# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.vals = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return self.vals
        self.inorderTraversal(root.left)
        self.vals.append(root.val)
        self.inorderTraversal(root.right)
        return self.vals