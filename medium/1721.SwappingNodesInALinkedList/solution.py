class Solution:
    def swapNodes(self, head, k):
        fast = start = head
        # using loop with k-1 step to find kth node from begin
        # then loop until fast is the end  to find kth node from end
        for _ in range(k-1):
            fast = fast.next
        end = fast
        while fast.next:
            fast = fast.next
            start = start.next
        end.val, start.val = start.val, end.val
        return head
