class Solution:
    def swapPairs(self, head):
        prev = None
        pivot = head
        Next = pivot.next
        while pivot and (Next := pivot.next):
            curr = pivot
            curr.next = Next.next
            Next.next = curr

            if not prev:
                head = Next
            else:
                prev.next = Next

            prev = curr
            pivot = curr.next
        return head
