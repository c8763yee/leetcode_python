# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_path(self, node, path):
        if node is None:
            return
        path.append(str(node.val))
        if not (node.left or node.right):
            self.dp.append('->'.join(path))

        else:
            self.get_path(node.left, path)
            self.get_path(node.right, path)
        path.pop()
        
    def binaryTreePaths(self, root):
        self.dp = []
        if not root:
            return self.dp
        self.get_path(root, [])
        return self.dp         