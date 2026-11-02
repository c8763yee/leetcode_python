
int sumCounts(int* nums, int numsSize) {
    int rets = 0;
    char count[101] = {0};

    for (int len = 1; len <= numsSize; len++) {
        int left = 0, right = 0, distinct = 0;
        memset(count, 0, 101);

        // Initialize the first window
        for (; right < len; right++) {
            if (count[nums[right]]++ == 0)
                distinct++;
        }
        rets += distinct * distinct;

        // Slide the window
        for (; right < numsSize; left++, right++) {
            if (count[nums[left]]-- == 1)
                distinct--;
            if (count[nums[right]]++ == 0)
                distinct++;

            rets += distinct * distinct;
        }
    }

    return rets;
}
