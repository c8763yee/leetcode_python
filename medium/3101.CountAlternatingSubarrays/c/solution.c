long long countAlternatingSubarrays(int* nums, int numsSize) {
    int left = 0;
    long long cnt = 0;
    for (int i = 0; i < numsSize; i++) {
        if (i && nums[i] == nums[i - 1]) {
            left = i;
        }

        cnt += i - left + 1;
    }
    return cnt;
}