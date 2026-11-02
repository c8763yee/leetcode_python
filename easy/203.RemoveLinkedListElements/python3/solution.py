# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# situation:
# 1. defaul
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        while head and head.val == val:
            head = head.next

        tmp = head
        while tmp:
            if not tmp.next:
                break
            while tmp.next and tmp.next.val == val:
                tmp.next = tmp.next.next
            tmp = tmp.next
        return head