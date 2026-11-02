# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

OR=2
AND=3
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """
        0: False
        1: True
        2: Or
        3: And
        """
        if not (root.left or root.right) or root.val <= 1:
            return root.val == 1
        if root.val == OR:
            return self.evaluateTree(getattr(root, 'left', 0)) or self.evaluateTree(getattr(root, 'right', 0))
        else:
            return self.evaluateTree(getattr(root, 'left', 0)) and self.evaluateTree(getattr(root, 'right', 0))