# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''
        self.text = [root.val]
        def traversal(node):
            if node is None:
                return
            self.text.append(f'({node.val}')
            if node.left:
                traversal(node.left)
            if node.right:
                if node.left is None:
                    self.text.append('()')
                traversal(node.right)       
        
            self.text.append(')')

        if root.left:
            traversal(root.left)
        if root.right:
            if root.left is None:
                self.text.append('()')
            traversal(root.right)
        return ''.join(map(str, self.text))
