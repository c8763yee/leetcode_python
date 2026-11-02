# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.nodes = []
        q = [root]
        
        
        while q: # O(log(n))
            self.nodes.append(q[-1].val)
            tmp = []
            for node in q:
                if node is None:
                    continue
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            q = tmp
        return self.nodes