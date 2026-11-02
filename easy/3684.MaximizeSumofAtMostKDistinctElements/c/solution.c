/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int lt(const void *a, const void *b){
    return (*(int *)a - *(int *)b);
}

int gt(const void *a, const void *b){
    return -(*(int *)a - *(int *)b);
}
int removeDuplicate(int *nums, int numsSize){
    int start = 0;
    int distinct = 1;
    for(int i=1;i<numsSize;i++){
        if (nums[start] == nums[i]){
            nums[i] = 0;
            continue;
        }
        distinct++;
        start = i;
    }
    return distinct;
}
int* maxKDistinct(int* nums, int numsSize, int k, int* returnSize) {
    qsort(nums, numsSize, sizeof(int), lt);
    int distinctSize = removeDuplicate(nums, numsSize);
    qsort(nums, numsSize, sizeof(int), gt);
    *returnSize = distinctSize<k?distinctSize:k;
    return nums;
    
}