int minMoves(int* nums, int numsSize) {
    int cnt = 0, largest = 0, maxval = 0;
    for(int i=0;i<numsSize;i++){
        maxval = nums[i]>maxval?nums[i]:maxval;
    }
    for(int i=0;i<numsSize;i++){
        if (nums[i]==maxval) continue;
        cnt += abs(nums[i]-maxval);
    }
    return cnt;
}