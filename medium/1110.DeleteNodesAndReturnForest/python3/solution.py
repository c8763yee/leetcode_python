# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []

    def dfs(self, root: TreeNode, to_delete: set, is_root: bool):   
        if (root is None):
            return root 

        is_to_delete = root.val in to_delete

        if is_to_delete is False and is_root:
            self.result.append(root)
        
        root.left = self.dfs(root.left, to_delete, is_to_delete)
        root.right = self.dfs(root.right, to_delete, is_to_delete)

        return None if is_to_delete else root

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        self.dfs(root, to_delete, True)
        return self.result

