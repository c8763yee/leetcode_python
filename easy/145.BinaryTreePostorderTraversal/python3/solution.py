# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None: return []
        stack = []
        ret = []
        last_visited = curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            node = stack[-1]
            if node.right and last_visited != node.right:
                curr = node.right
            else:
                ret.append(node.val)
                last_visited = stack.pop()

        return ret
        