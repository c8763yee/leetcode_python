

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int isSelfDividing(int num_orig){
    int num = num_orig;
    int n;
    if (num == 0) return 0;
    while (num!=0){
        n = num%10;
        if (n==0||num_orig%n) return 0;
        num /=10;
    }
    return 1;
}

int* selfDividingNumbers(int left, int right, int* returnSize){
    int *arr = (int*)malloc(10000 * sizeof(int));
    int idx = 0;
    for (int i=left; i<=right; i++){
        if (isSelfDividing(i)){
            arr[idx++] = i;
        }
        
    }
    *returnSize = idx;
    return arr;
}