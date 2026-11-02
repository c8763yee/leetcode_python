class MyQueue:

    def __init__(self):
        self.stack = []
        self.inner = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            self.inner.append(self.stack.pop())
        
        val = self.inner.pop()
        while self.inner:
            self.stack.append(self.inner.pop())

        return val

    def peek(self) -> int:
        return self.stack[0] if self.stack != [] else self.inner[-1]

    def empty(self) -> bool:
        return self.stack == [] and self.inner == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()