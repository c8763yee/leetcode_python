int sumOfUnique(int* nums, int numsSize) {
    int s[101];
    int sums = 0;
    memset(s, 0, 101);
    for (int i = 0; i < numsSize; i++) {

        if (s[nums[i]]) {
            if (s[nums[i]] == 1) {
                s[nums[i]] = 2;
                sums -= nums[i];
            }
        } else {
            sums += nums[i];
            s[nums[i]] = 1;
        }
    }
    return sums;
}