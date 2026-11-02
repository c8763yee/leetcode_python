# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0

        q = [root]
        result = []
        while q:
            temp = []
            sum_val = 0
            for ele in q:
                if ele is None:
                    continue
                sum_val += ele.val
                temp.append(ele.left)
                temp.append(ele.right)

            result.append(sum_val)
            q = temp
        if k >= len(result):
            return -1
        return sorted(result, reverse=True)[k-1] # 1-indexed
        