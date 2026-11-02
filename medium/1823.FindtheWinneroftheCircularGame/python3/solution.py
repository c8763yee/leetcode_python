class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque(range(1, n+1))
        for _ in range(n-1):
            queue.rotate(-k+1)
            queue.popleft()
        return queue.pop()