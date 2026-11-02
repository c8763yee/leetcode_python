# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(hnode: Optional[ListNode]) -> ListNode:
    prev = next_node = None
    node = hnode
    while node:
        next_node = node.next
        node.next = prev
        prev = node
        node = next_node

    return prev

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None: # there's only one node
            return True
        elif head.next.next is None:
            return head.val == head.next.val
        
        slow = head
        fast = head.next
        # get middle of node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next
        node = reverse(slow)
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True