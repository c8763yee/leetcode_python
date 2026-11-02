# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = None
        node = None
        val = 0
        while head:
            if head.val != 0:
                val += head.val
            elif root:
                node.next = ListNode(val)
                node = node.next
                val = 0
            elif val != 0:
                root = node = ListNode(val)
                val = 0
            head = head.next               

        return root 
                    
