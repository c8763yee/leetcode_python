int minCost(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0], x = 0;
    bool dp[m][n][1024];
    memset(dp, false, 1024 * m * n * sizeof(bool));
    dp[m - 1][n - 1][grid[m - 1][n - 1]] = true;
    for (int i = m - 1; i >= 0; --i) {
        for (int j = n - 1; j >= 0; --j) {
            for (int x = 0; x < 1024; ++x) {
                if (i + 1 < m)
                    dp[i][j][x] |= dp[i + 1][j][x ^ grid[i][j]];

                if (j + 1 < n)
                    dp[i][j][x] |= dp[i][j + 1][x ^ grid[i][j]];
            }
        }
    }

    for (x = 0; x < 1024; ++x) {
        if (dp[0][0][x])
            return x;
    }
    return -1;
}