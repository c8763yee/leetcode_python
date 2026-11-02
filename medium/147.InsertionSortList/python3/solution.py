# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst2 = []
        while head:
            lst2.append(head.val)
            head = head.next
        lst2.sort()
        for lst in lst2:
            if head is None:
                head = node = ListNode(val=lst)
                continue
            node.next = ListNode(val=lst)
            node = node.next        
        return head