# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        index = 1
        local_minima = local_maxima = -1

        before = None
        after = head.next

        critical = []

        while head and head.next:
            if not (before and after):
                pass
            elif (
                before.val < head.val
                and head.val > after.val
                or before.val > head.val
                and head.val < after.val
            ):

                critical.append(index)

            before = head
            head = after
            after = head.next

            index += 1



        if index < 3 or len(critical) < 2:
            return [-1, -1]

        max_dist = max(critical) - min(critical)
        min_dist = float('inf')
        critical.sort()
        
        # finding maximum and minimum distance between crital points
        for i in range(1, len(critical)):
            dist = abs(critical[i]-critical[i-1])
            min_dist = min(min_dist, dist)

        return [min_dist, max_dist]
