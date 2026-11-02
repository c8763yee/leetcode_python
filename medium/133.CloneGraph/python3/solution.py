"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(cur_node):
            if cur_node is None:
                return None
            if cur_node in visited:
                return visited[cur_node]

            new_node = Node(cur_node.val)
            visited[cur_node] = new_node
            for neighbor in cur_node.neighbors:
                new_node.neighbors.append(dfs(neighbor))

            return new_node


        return dfs(node)
        
            
            
