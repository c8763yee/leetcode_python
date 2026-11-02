int evenNumberBitwiseORs(int* nums, int numsSize) {
    int bw = 0;
    for(int i=0;i<numsSize;i++){
        if (nums[i]%2==0) bw |= nums[i];
    }
    return bw;
}