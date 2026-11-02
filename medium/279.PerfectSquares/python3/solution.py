class Solution:
    def numSquares(self, n: int) -> int:
        queue = [n]
        level = 1
        while queue:
            tmp_queue = []
            for n in queue:
                for i in range(round(sqrt(n)+0.5), 0, -1):
                    if i*i > n:
                        continue
                    if n-i*i == 0:
                        return level
                    tmp_queue.append(n-i*i)
            
            queue = tmp_queue
            level += 1
        return 0
                