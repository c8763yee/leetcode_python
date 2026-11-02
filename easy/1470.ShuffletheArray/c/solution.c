

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    if(numsSize == 1){return nums;}
    *returnSize = numsSize;
    int* arr = (int*)malloc(sizeof(int)*numsSize);
    for(int i=0;i<numsSize;i++){ //even x_i, odd(x_i+n)
        arr[i] = nums[(i/2)+n*(i%2)];
    }
    return arr;
}