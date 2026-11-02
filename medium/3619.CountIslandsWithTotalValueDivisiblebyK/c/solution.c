const int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};
int dfs(int **grid, int rows, int cols,
        int i, int j, int k, int *stack)
{
    int top = 0;
    int rem = grid[i][j] % k;

    grid[i][j] = 0;
    stack[top++] = i * cols + j;

    while (top) {
        int pos = stack[--top];
        int r = pos / cols;
        int c = pos % cols;

        for (int t = 0; t < 4; t++) {
            int nr = r + dy[t];
            int nc = c + dx[t];

            if (nr < 0 || nr >= rows ||
                nc < 0 || nc >= cols ||
                grid[nr][nc] == 0)
                continue;

            rem = (rem + grid[nr][nc]) % k;
            grid[nr][nc] = 0;
            stack[top++] = nr * cols + nc;
        }
    }

    return rem == 0;
}
int countIslands(int **grid, int gridSize,
                 int *gridColSize, int k)
{
    int rows = gridSize;
    if (!rows)
        return 0;

    int cols = gridColSize[0];
    if (!cols)
        return 0;

    int count = 0;
    int *stack = malloc((size_t)rows * cols * sizeof(*stack));
    if (!stack)
        return -1;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == 0)
                continue;

            count += dfs(grid, rows, cols, i, j, k, stack);
        }
    }

    free(stack);
    return count;
}