/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int *ans = malloc(sizeof(int) * numsSize);
    ans[0] = 1;
    int fix = 1; // prefix for now
    for (int i=1;i<numsSize;i++){
        ans[i] = nums[i-1]*fix;
        fix *= nums[i-1];
    }

    fix = 1; // now it become suffix
    for (int i=numsSize-1;i>=0;i--){
        ans[i] *= fix;
        fix *= nums[i];
    }

    *returnSize = numsSize;
    return ans;
}