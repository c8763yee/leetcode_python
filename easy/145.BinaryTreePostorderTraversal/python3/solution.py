# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dp = []
    def pt(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.dp.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]):
        self.pt(root)
        return self.dp