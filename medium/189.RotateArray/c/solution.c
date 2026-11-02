void reverse_range(int* nums, int start, int end) {
    int tmp;
    while (start < end) {
        tmp = nums[start];
        nums[start++] = nums[end];
        nums[end--] = tmp;
    }
}
void rotate(int* nums, int numsSize, int k) {
    k %= numsSize;
    reverse_range(nums, 0, numsSize - 1);
    reverse_range(nums, 0, k - 1);
    reverse_range(nums, k, numsSize - 1);
}