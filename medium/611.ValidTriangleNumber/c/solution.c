int cmp(const void* a, const void* b) { return *(int*)a - *(int*)b; }
void merge(int arr[], int start, int mid, int end)
{
    int start2 = mid + 1;

    // If the direct merge is already sorted
    if (arr[mid] <= arr[start2]) {
        return;
    }

    // Two pointers to maintain start
    // of both arrays to merge
    while (start <= mid && start2 <= end) {

        // If element 1 is in right place
        if (arr[start] <= arr[start2]) {
            start++;
        }
        else {
            int value = arr[start2];
            int index = start2;

            // Shift all the elements between element 1
            // element 2, right by 1.
            while (index != start) {
                arr[index] = arr[index - 1];
                index--;
            }
            arr[start] = value;

            // Update all the pointers
            start++;
            mid++;
            start2++;
        }
    }
}
void sort(int *arr, int start, int end){
    if (start >= end)return;
    int mid = start + ((end-start) >> 1);
    sort(arr, start, mid);
    sort(arr, mid+1, end);
    merge(arr, start, mid, end);

}
int triangleNumber(int* nums, int numsSize) {
    sort(nums, 0, numsSize-1);
    int a = 0, b = 0, count = 0;
    for (int c = numsSize - 1; c >= 2; c--) {
        a = 0;
        b = c - 1;
        while (a < b) {
            if (nums[a] + nums[b] > nums[c]) {
                count += (b - a);
                b--;
            } else {
                a++;
            }
        }
    }
    return count;
}