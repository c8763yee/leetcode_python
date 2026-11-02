void traverse(char** grid, int gridSize, int gridColSize, int i, int j) {
    if (grid[i][j] == '0')
        return;
    grid[i][j] = '0';
    if (j < gridColSize - 1)
        traverse(grid, gridSize, gridColSize, i, j + 1);
    if (i < gridSize - 1)
        traverse(grid, gridSize, gridColSize, i + 1, j);
    if (j > 0)
        traverse(grid, gridSize, gridColSize, i, j - 1);
    if (i > 0)
        traverse(grid, gridSize, gridColSize, i - 1, j);
}

int numIslands(char** grid, int gridSize, int* gridColSize) {
    int islands = 0;
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            if (grid[i][j] != '1')
                continue;
            traverse(grid, gridSize, gridColSize[i], i, j);
            islands++;
        }
    }
    return islands;
}