long long countSubarrays(int* nums, int numsSize, int minK, int maxK) {
    long long cnt = 0;
    for (int i = 0, left = 0; i < numsSize; i++) {
        if (nums[i] < minK || nums[i] > maxK) {
            left = i + 1;
        } else {
            cnt += i - left + 1;
        }
    }
    return cnt;
}