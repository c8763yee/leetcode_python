/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* grayCode(int n, int* returnSize) {
    *returnSize=(1<<n);
    int *arr = calloc(*returnSize, sizeof(int));
    for(int i=1;i<(*returnSize);i++){
       arr[i] = i^(i>>1); 
    }
    return arr;
    // 0000 0000
    // 0001 0001
    // 0011 0010
    // 0010 0011
    // 0110 0100
    // 0111 0101
    // 0101 0110
    // 0100 0111
}