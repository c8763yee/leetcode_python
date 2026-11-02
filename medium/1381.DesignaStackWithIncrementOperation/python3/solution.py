class CustomStack:
    def is_full(self):
        return self.size == self.maxSize     
    
    def is_empty(self):
        return self.top == -1
    
    def __init__(self, maxSize: int):
        self.maxSize = maxSize    
        self.arr = [None for _ in range(maxSize)]
        self.size = 0
        self.top = -1
        
    def push(self, value: int) -> None:
        if self.is_full() is False:
            self.top += 1
            self.size += 1
            self.arr[self.top] = value

    def pop(self) -> int:
        if self.is_empty():
            return -1
        tmp = self.arr[self.top]
        self.top -= 1
        self.size -= 1
        return tmp
        
    def increment(self, k: int, val: int) -> None:
        k = min(k, self.size)
        for i in range(k):
            self.arr[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)