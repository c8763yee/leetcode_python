int removeDuplicates(int* nums, int numsSize) {
    int valid = 0;
    int visited[20001] = {0};
    for(int i=0;i<numsSize;i++){
        if (visited[nums[i]+10000]==2) continue;
        nums[valid++] = nums[i];
        visited[nums[i]+10000]++;
    }
    return valid;
}