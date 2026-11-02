class LRUCache:

    def __init__(self, capacity: int):
        self.index = 0
        self.lru = {}
        self.recent_used = {}
        self.capacity = capacity
        self.index = 0

    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        self.index += 1
        self.recent_used[key] = self.index
        return self.lru[key]

    def put(self, key: int, value: int) -> None:
        self.index += 1
        if key in self.lru:
            self.lru[key] = value
            self.recent_used[key] = self.index
            return

        if len(self.recent_used) >= self.capacity:
            element = min(self.lru, key=self.recent_used.get)
            self.lru.pop(element)
            self.recent_used.pop(element)

        self.lru[key] = value
        self.recent_used[key] = self.index


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)