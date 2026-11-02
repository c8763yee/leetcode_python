# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return (
                p.val == q.val
                and isSameTree(p.left, q.left)
                and isSameTree(p.right, q.right)
            )

        def traversal(root: Optional[TreeNode]) -> bool:
            if root is None:
                return False
            if isSameTree(root, subRoot):
                return True
            return traversal(root.left) or traversal(root.right)

        return traversal(root)

