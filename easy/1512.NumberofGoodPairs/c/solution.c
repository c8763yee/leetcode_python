int numIdenticalPairs(int* nums, int numsSize) {
    int cnt = 0;
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            cnt += nums[i] == nums[j];
        }
    }
    return cnt;
}