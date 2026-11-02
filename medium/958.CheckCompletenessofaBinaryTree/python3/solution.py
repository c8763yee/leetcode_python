# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = [root]
        flag = False

        while q:
            tmp = []
            for node in q:
                if not node:
                   flag = True
                   continue
                if flag:
                    return False
                tmp.append(node.left)
                tmp.append(node.right)

            q = tmp
        return True