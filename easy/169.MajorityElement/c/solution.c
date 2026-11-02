int majorityElement(int* nums, int numsSize) {
    int cnt = 0;
    int maj;
    for(int i=0;i<numsSize;i++){
        if (cnt == 0){
            maj = nums[i];
            cnt++;
        }else{
            cnt += nums[i]==maj?1:-1;
        }
    }
    return maj;
}