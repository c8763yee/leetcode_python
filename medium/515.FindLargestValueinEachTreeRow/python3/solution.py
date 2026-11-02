# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        row = []
        if root is None:
            return []
        q = [root]
        while q:
            lst = []
            max_val = -2**31
            for i in q:
                if i is None:
                    continue
                if i.left:
                    lst.append(i.left)
                if i.right:
                    lst.append(i.right)
                if max_val < i.val:
                    max_val = i.val
            q = lst
            row.append(max_val)
        return row