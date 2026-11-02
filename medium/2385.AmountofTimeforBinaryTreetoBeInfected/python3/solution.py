# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # convert tree to adj list
        adj = defaultdict(set)
        def convert_adj(node):
            if node is None or not (node.left or node.right):
                return False

            if node.left:
                adj[node.val].add(node.left.val)
                adj[node.left.val].add(node.val)
                convert_adj(node.left)

            if node.right:
                adj[node.val].add(node.right.val)
                adj[node.right.val].add(node.val)
                convert_adj(node.right)
            return True

        if convert_adj(root) is False:
            return int(start != root.val)
        print(adj)
        visited = dict.fromkeys(adj.keys(), False)
        def dfs(n):
            if visited[n]:
                return 0
            
            count = 0
            visited[n] = True
            for i in adj[n]:
                count = max(count, dfs(i)+1)
            visited[n] = False
            return count

        return dfs(start)-1