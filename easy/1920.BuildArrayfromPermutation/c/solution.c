

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* buildArray(int* nums, int numsSize, int* returnSize){
    int *newArr = malloc(4*numsSize), i=0;
    *returnSize = numsSize;
    for(i;i<numsSize;i++){
        newArr[i] = nums[nums[i]];
    }
    return newArr;
    
}