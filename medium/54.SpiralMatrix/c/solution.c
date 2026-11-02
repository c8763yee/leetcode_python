/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* spiralOrder(int** matrix, int matrixSize, int* matrixColSize,
                 int* returnSize) {
    int idx = 0;
    int m = matrixSize, n = matrixColSize[0];
    *returnSize = m * n;

    bool visited[m][n];
    memset(visited, false, m * n * sizeof(bool));

    int* dp = malloc(sizeof(int) * m * n);
    memset(dp, 0, sizeof(int) * m * n);

    int top = 0, bottom = m - 1;
    int left = 0, right = n - 1;
    int direction = 0, di[4] = {0, 1, 0, -1}, dj[4] = {1, 0, -1, 0};
    int i = 0, j = 0;
    while (idx < m * n) {
        visited[i][j] = true;
        dp[idx++] = matrix[i][j];
        int ni = i + di[direction];
        int nj = j + dj[direction];

        if (ni < 0 || ni >= m || nj < 0 || nj >= n || visited[ni][nj]) {
            direction = (direction + 1) % 4;
            i += di[direction];
            j += dj[direction];
        } else {
            i = ni;
            j = nj;
        }
    }

    return dp;
}