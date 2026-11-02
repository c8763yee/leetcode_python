int removeElement(int* nums, int numsSize, int val) {
    int valid=0;
    
    for(int i=0;i<numsSize;i++){
        if (nums[i] != val) nums[valid++] = nums[i];
    }
    return valid;
}