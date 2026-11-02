class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row = len(isWater)
        col = len(isWater[0])

        # Iterative through the matrix from top left to bottom right
        # to check if left or top side can be walked into 0
        # and initialize at same time
        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    isWater[i][j] = 0
                    continue
                
                isWater[i][j] = float('inf')

                if j > 0:
                    isWater[i][j] = min(isWater[i][j], isWater[i][j - 1] + 1)
                if i > 0:
                    isWater[i][j] = min(isWater[i][j], isWater[i - 1][j] + 1)

        # Iterative backwards through the matrix from bottom right to top left
        # to check if right or bottom side of neighbor is nearest path to 0
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                if isWater[i][j] <=1:
                    continue

                if i < row - 1:
                    isWater[i][j] = min(isWater[i][j], isWater[i + 1][j] + 1)
                if j < col - 1:
                    isWater[i][j] = min(isWater[i][j], isWater[i][j + 1] + 1)

        return isWater  # all mat elements are 0