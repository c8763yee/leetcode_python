class Solution:
    def addTwoNumbers(self, l1, l2):
        start = None
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            val = v1 + v2 + carry
            carry = val // 10
            node = ListNode(val % 10)
            if not start:
                start = curr = node
                continue
            curr.next = node
            curr = curr.next
        return start

