/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

bool containZero(int n) {
    while (n) {
        if (n % 10 == 0)
            return true;
        n /= 10;
    }
    return false;
}
int* getNoZeroIntegers(int n, int* returnSize) {
    int* ab = (int*)calloc(2, sizeof(int));
    int max = n, min = 1, mid = 0;
    *returnSize = 2;
    while (min < max) {
        mid = min+(max-min)/2;
        if (!(containZero(mid) || containZero(n - mid))) {
            ab[0] = mid;
            ab[1] = n - mid;
            break;
        }
        else
            max = mid;
    }
    return ab;
}