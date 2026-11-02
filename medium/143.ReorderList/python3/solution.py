class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev, node = None, slow
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node

        # Merge the two halves
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next