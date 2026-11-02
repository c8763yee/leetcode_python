#define abs(a) ((a) < 0 ? -(a) : (a))

int findClosest(int x, int y, int z) {
    int diff_x = abs(x - z);
    int diff_y = abs(y - z);

    if (diff_x == diff_y) {
        return 0;
    } else if (diff_x < diff_y) {
        return 1;
    } else {
        return 2;
    }
}