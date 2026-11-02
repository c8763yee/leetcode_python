# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.size=0
        tmp = head
        while tmp:
            tmp = tmp.next
            self.size += 1
        del tmp

    def getRandom(self) -> int:
        tmp = self.head
        for i in range(random.randrange(self.size)):
            tmp  = tmp.next
        return tmp.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()