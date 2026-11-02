class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        if self.min_heap == []:
            return
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        if not self.min_heap:
            self.min_heap = [val]
            return val
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif self.min_heap[0] < val:
            heapq.heappushpop(self.min_heap, val)
        return self.min_heap[0]
