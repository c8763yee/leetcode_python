class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.max = k
        self.len = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue.append(value)
        self.len += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue.pop(0)
        self.len -= 1
        return True
        

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[0]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.len-1]

    def isEmpty(self) -> bool:
        return self.len == 0
    
    def isFull(self) -> bool:
        return self.len == self.max