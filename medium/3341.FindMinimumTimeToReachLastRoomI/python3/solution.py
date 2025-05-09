class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dist = [[float("inf")] * m for _ in range(n)]
        dist[0][0] = 0

        heap = [(0, 0, 0)]  # (time, row, col)

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while heap:
            t, i, j = heapq.heappop(heap)

            if (i, j) == (n - 1, m - 1):
                return t

            if t > dist[i][j]:
                continue

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    arrive = max(t, moveTime[ni][nj]) + 1
                    if arrive < dist[ni][nj]:
                        dist[ni][nj] = arrive
                        heapq.heappush(heap, (arrive, ni, nj))
