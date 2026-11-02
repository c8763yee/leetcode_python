"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.lst=[]

    def post(self, node):
        if node is None:
            return
        for i in node.children:
            self.post(i)
            self.lst.append(i.val)
    def postorder(self, root: 'Node') -> List[int]:
        self.post( root)
        if root:
            self.lst.append(root.val)
        return self.lst