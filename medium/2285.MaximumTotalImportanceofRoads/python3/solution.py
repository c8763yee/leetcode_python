class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        conn = [0 for _ in range(n)]
        for i, j in roads:
            conn[i] += 1
            conn[j] += 1

        conn.sort()

        cost = 1
        result = 0
        for d in conn:
            result += cost * d
            cost += 1
        return result
