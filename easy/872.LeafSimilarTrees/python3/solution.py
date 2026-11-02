# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_leaf = []
        root2_leaf = []
        def preorder(node, arr):

            if node is None:
                return

            if node.left is None and node.right is None:
                arr.append(node.val)

            preorder(node.left, arr)
            preorder(node.right, arr)

        preorder(root1, root1_leaf)
        preorder(root2, root2_leaf)

        return root1_leaf == root2_leaf

        