# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def enqueue(self, n: int):
        node = ListNode(val=n)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
            
        return True

    def dequeue(self):
        if self.head is None:
            return None
        val = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return val

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
        queue_below = Queue()
        queue_above = Queue()
        ptr = head
        while ptr:
            if ptr.val < x:
                queue_below.enqueue(ptr.val)
            else:
                queue_above.enqueue(ptr.val)

            ptr = ptr.next
        if queue_below.head:
            queue_below.tail.next = queue_above.head
            return queue_below.head
        return queue_above.head

        