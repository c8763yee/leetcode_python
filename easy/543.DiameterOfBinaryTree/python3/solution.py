# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def get_diameter(node: TreeNode) -> tuple[int, int]:
            if node is None:
                return 0, 0

            left_length, left_diameter = get_diameter(node.left)
            right_length, right_diameter = get_diameter(node.right)
            return max(left_length, right_length) + 1, max(left_length + right_length, left_diameter, right_diameter)

        if root is None:
            return 0

        _, diameter = get_diameter(root)
        return diameter
