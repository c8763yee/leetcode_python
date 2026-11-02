# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1
        index = 1
        while head and not a <= index <= b:
            head = head.next
            index += 1

        remain = head.next
        head.next = list2
        for _ in range(b-a+1): # inclusive
            remain = remain.next
        
        while head.next:
            head = head.next
        head.next = remain
        return list1