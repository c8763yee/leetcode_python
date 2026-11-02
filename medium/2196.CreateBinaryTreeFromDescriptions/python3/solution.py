# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree = {}
        childs = set()
        for value, child, direction in descriptions:
            if tree.get(child) is None:
                tree[child] = TreeNode(child)

            if tree.get(value) is None:
                tree[value] = TreeNode(value)

            setattr(tree[value], "left" if direction else "right", tree[child])

            childs.add(child)

        for value in tree:
            if value not in childs:
                return tree[value]
        return None
