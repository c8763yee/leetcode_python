# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = 0
        node = head
        while node:
            val = val * 10 + node.val
            node = node.next

        val *= 2
        if val == 0:
            return ListNode(0)
        new = ListNode(val%10)
        val //= 10
        while val:
            new = ListNode(val%10, new)
            val //= 10
        return new

