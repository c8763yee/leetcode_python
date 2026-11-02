class ListNode:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_

class MyLinkedList:
    def __init__(self):
        self.root = None
        self.tail = None

    def getNode(self, index: int) -> ListNode:
        node = self.root
        for i in range(index):
            if node is None:
                return None
            node = node.next
        return node

    def get(self, index: int) -> int:
        node = self.getNode(index)
        return node.val if node else -1

    def addAtRoot(self, val) -> None:
        self.root = self.tail = ListNode(val)

    def addAtHead(self, val: int) -> None:
        if self.root is None:
            return self.addAtRoot(val)
        new_node = ListNode(val, self.root)
        self.root = new_node

    def addAtTail(self, val: int) -> None:
        if self.root is None:
            return self.addAtRoot(val)
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)
        prev_node = self.getNode(index - 1)
        if prev_node is None:
            return
        new_node = ListNode(val, prev_node.next)
        prev_node.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def deleteAtIndex(self, index: int) -> None:
        if self.root is None:
            return
        if index == 0:
            self.root = self.root.next
            if self.root is None:
                self.tail = None
            return
        prev_node = self.getNode(index - 1)
        if prev_node is None or prev_node.next is None:
            return
        prev_node.next = prev_node.next.next
        if prev_node.next is None:
            self.tail = prev_node
