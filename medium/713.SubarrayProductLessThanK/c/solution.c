int numSubarrayProductLessThanK(int* nums, int numsSize, int k) {
    int ret = 0, prod = 1;
    if (k <= 1) return 0;
    for(int left = 0, right = 0; right < numsSize; right++){
        prod *= nums[right];
        while (prod >=k && left <= right){
            prod /=nums[left];
            left++;
        }
        ret += right - left + 1;
    }
    return ret;
}