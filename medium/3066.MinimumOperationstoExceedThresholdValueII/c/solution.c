void heapify(int* arr, int i, int n) {
    while (1) {
        int smallest = i;
        int left = (i << 1) + 1;
        int right = (i << 1) + 2;

        if (left < n && arr[left] < arr[smallest]) {
            smallest = left;
        }

        if (right < n && arr[right] < arr[smallest]) {
            smallest = right;
        }

        if (smallest == i)
            break;

        int swap = arr[i];
        arr[i] = arr[smallest];
        arr[smallest] = swap;
        i = smallest;
    }
}

void buildHeap(int* arr, int size) {
    for (int i = (size >> 1) - 1; i >= 0; i--) {
        heapify(arr, i, size);
    }
}

static inline bool mulOvf(int n) { return INT_MAX >> 1 < n; }
static inline bool addOvf(int a, int b) {
    return a > 0 && b > 0 && (INT_MAX - b < a);
}

int minOperations(int* nums, int numsSize, int k) {
    for (int i=0; i<numsSize;i++){
        if(nums[i]>=k)nums[i] = INT_MAX;
    }
    buildHeap(nums, numsSize);
    if (*nums >= k)
        return 0;

    int top, val, count = 0;
    for (int i = 0; i < numsSize - 1; i++) {
        top = *nums;
        *nums = INT_MAX;
        heapify(nums, 0, numsSize);
        if (mulOvf(top) || addOvf(top << 1, *nums))
            *nums = k;
        else {
            val = (top << 1) + *nums;
            *nums = val;
        }
        heapify(nums, 0, numsSize);
        count++;
        if (*nums >= k)
            break;
    }
    return count;
}