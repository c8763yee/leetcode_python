class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        def merge(l1, l2):
            if not (l1 and l2):
                return l1 or l2
            if l1.val < l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            l2.next = merge(l1, l2.next)
            return l2
        def lenLList(node):
            size = 0
            while node:
                size += 1
                node = node.next
            return size
        lists.sort(key=lenLList, reverse=True)
        node = lists.pop()
        while lists:
            node = merge(node, lists.pop())
        return node
