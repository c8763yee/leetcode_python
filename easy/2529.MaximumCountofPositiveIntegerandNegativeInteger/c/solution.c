int maximumCount(int* nums, int numsSize) {
    int pos=0, neg=0;
    for(int i=0;i<numsSize;i++){
        if (nums[i])
        nums[i]>0?pos++:neg++;
    }
    
    return pos-neg>0?pos:neg;
}