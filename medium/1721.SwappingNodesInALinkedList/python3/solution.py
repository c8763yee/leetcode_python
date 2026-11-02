class Solution:
    def swapNodes(self, head, k):
        fast = start = head
        # using loop with k-1 step to find kth node from begin
        # then loop untl  to find kth node from endj
        for _ in range(k-1):
            fast = fast.next
        end = fast
        while fast.next:
            fast = fast.next
            start = start.next
        end.val, start.val = start.val, end.val
        return head      