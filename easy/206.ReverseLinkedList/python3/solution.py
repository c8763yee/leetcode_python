# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        # Intuition:
        iterate through the list and 
        1. store next node
        2. set next node to previous node
        3. set previous node to current node
        4. set current node to stored next node

        Args:
            head (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """
        node = head
        next_node = prev_node = None
        while node:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node

        return prev_node