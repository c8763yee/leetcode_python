class List:
    def __init__(self, val=None, Next=None):
        self.val = val
        self.next = Next
class MyHashSet:

    def __init__(self):
        self.size = 256
        self.values = [List(-1) for _ in range(self.size)]
    def hash(self, a):
        return ((a*1048583&(1<<21)-1) % self.size)

    def add(self, key: int) -> None:
        value = self.hash(key)
        node = self.values[value]
        # collision process
        # keep finding until reach bottom or found itself
        while node.next:
            if node.next.val == key:
                return
            node = node.next
        node.next = List(key)
        
    def remove(self, key: int) -> None:
        value = self.hash(key)
        node = self.values[value]
        # collision process
        while node.next:
            if node.next.val == key:
                node.next = node.next.next
                return
            node = node.next

        
    def contains(self, key: int) -> bool:
        value = self.hash(key)
        node = self.values[value]
        while node.next:
            if node.next.val == key:
                return True
            node = node.next
        return node.val == key

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)