/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** createGrid(int m, int n, int* returnSize) {
    char** grid =
        (char**)malloc(m * sizeof(char*)); // Allocate pointer array first

    for (int i = 0; i < m; i++) {
        grid[i] = (char*)malloc((n + 1) * sizeof(char)); // +1 for '\0'
        memset(grid[i], '#', n);                         // Fill with '#'
        grid[i][n] = '\0';                               // Null terminate
    }
    int i = 0, j = 0, dx = 1, dy = 0;

    while (1) {
        grid[i][j] = '.';
        if (i==m-1 && j==n-1) break;

        if (dy && i+dy < m)
            i += dy;
        else if (dx && j+dx<n)
            j += dx;
        dy = !dy;
        dx = !dx;
    }

    *returnSize = m;
    return grid;
}