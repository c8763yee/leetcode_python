int cmp(const void *a, const void *b){
    int _a = *(int *)a;
    int _b = *(int *)b;
    return _a*_a > _b*_b;
}

long long maxAlternatingSum(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), cmp);
    long long cnt = 0;
    int e = 0;
    for(int i=0;i<numsSize; i++){
        e = nums[i];
        cnt += e*e*(i>=(numsSize>>1)?1:-1);
    }
    return cnt;
}