MAX_INT = 10001

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[0 if i == j else MAX_INT for j in range(n)] for i in range(n)]
        for src, dst, weight in edges:
            dp[src][dst] = weight
            dp[dst][src] = weight

        # floyd warshell
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][k] + dp[k][j] < dp[i][j]:
                        dp[i][j] = dp[i][k] + dp[k][j]

        min_distance = MAX_INT
        max_city = 0
        for city in range(n):
            distance = 0
            for walk in range(n):
                if dp[city][walk] <= distanceThreshold:
                    distance += 1
                    
            if distance <= min_distance:
                max_city = city
                min_distance = distance
                
        return max_city