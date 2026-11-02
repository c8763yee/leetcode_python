int* runningSum(int* nums, int numsSize, int* returnSize){
    *returnSize = numsSize;
    if (numsSize == 1){return nums;}
    for (int i = 1; i < numsSize; i++)
    {
        *(nums+i) += *(nums+i-1);
    }
    return nums;
}