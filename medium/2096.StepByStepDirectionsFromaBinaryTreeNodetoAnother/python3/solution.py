# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_LCA(self, node: TreeNode | None, p: int, q: int) -> TreeNode | None:
        if node is None or node.val == p or node.val == q:
            return node

        left_node = self.find_LCA(node.left, p, q)
        right_node = self.find_LCA(node.right, p, q)

        if left_node and right_node:
            return node

        return left_node if left_node else right_node

    def traversal(self, node: TreeNode | None, target: int, words:list) -> bool:
        if node is None:
            return False
        if node.val == target:
            return True

        words.append('L')
        if self.traversal(node.left, target, words):
            return True
        words.pop()

        words.append('R')
        if self.traversal(node.right, target, words):
            return True
        words.pop()
        return False

    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        lca = self.find_LCA(root, startValue, destValue)
        left_path = []
        right_path = []

        self.traversal(lca, startValue, left_path)
        self.traversal(lca, destValue, right_path)

        index = 0
        while (
            index < len(left_path)
            and index < len(right_path)
            and left_path[index] == right_path[index]
        ):
            index += 1
            
        return ("U" * (len(left_path) - index)) + ''.join(right_path[index:])
