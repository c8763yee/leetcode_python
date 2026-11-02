# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head

        def get_len(node):
            length = 0
            while node:
                length += 1
                node = node.next

            return length

        size = get_len(head)

        if size == 1 or k % size == 0:
            return head

        k %= size
        # apply fast-slow pointer (diff=n)
        fast = slow = pivot = head
        for _ in range(k):
            fast = fast.next

        while fast:
            if fast.next is None:
                pivot = slow
            fast = fast.next
            slow = slow.next

        # cut list into two part
        pivot.next = None

        # find tail of slow pointer and put next node into it
        pivot = slow
        while pivot.next:
            pivot = pivot.next
        pivot.next = head

        return slow
