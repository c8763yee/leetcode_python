class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def heapify(root, size):
            largest_child = root*2+1
            if largest_child >= size:
                return
            if largest_child+1 < size and stones[largest_child+1] > stones[largest_child]:
                largest_child += 1  
            if stones[root] < stones[largest_child]:
                stones[root], stones[largest_child] = stones[largest_child], stones[root]
                heapify(largest_child, size)
        def init_heapify(size):
            for idx in range(size // 2, -1,-1):
                heapify(idx, size)
        def heap_sort(size):
            init_heapify(size)
            for idx in range(size-1, 0, -1):
                stones[0], stones[idx] = stones[idx], stones[0]
                heapify(0, idx)
        size = len(stones)
        heap_sort(size)
        while stones:
            last = stones.pop()
            if not stones:
                return last
            last2 = stones.pop()
            if last != last2:
                insort_left(stones, last-last2)
        return 0