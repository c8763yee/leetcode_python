class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """Uses a 2D array to store the distance of each cell to the nearest 0.
        dp[i][j] is the distance of mat[i][j] to the nearest 0.

        Args:
            mat (List[List[int]]): _description_

        Returns:
            List[List[int]]: _description_
        """

        row = len(mat)
        col = len(mat[0])
        dp = [
            [0 if mat[i][j] == 0 else float("inf") for j in range(col)]
            for i in range(row)
        ]

        # Iterative through the matrix from top left to bottom right
        # to check if previous steps have 0 or less distance
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    continue
                # check x axis
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
                # check y axis
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)

        # Iterative backwards through the matrix from bottom right to top left
        # to check if next steps have 0 or less distance

        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                if mat[i][j] == 0:
                    continue
                if i < row - 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j < col - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        return dp  # all mat elements are 0
