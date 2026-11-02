bool isDivisibleBy3(int n){
  
    
    return (n%3) == 0;
}

int averageValue(int* nums, int numsSize) {
    int count = 0;
    int val = 0;
    for(int i=0;i<numsSize;i++){
        if ((nums[i]&1)==0 && isDivisibleBy3(nums[i])) {
            val += nums[i];
            count++;
        }
    }
    if (count == 0)return 0;
    return val / count;
}