#define min(a, b) a < b ? a : b

int earliestTime(int** tasks, int tasksSize, int* tasksColSize) {
    int minTime = INT_MAX;
    int s, t;
    for (int i = 0; i < tasksSize; i++) {
        minTime = min(minTime, tasks[i][0] + tasks[i][1]);
    }
    return minTime;
}