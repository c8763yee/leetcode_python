int removeDuplicates(int* nums, int numsSize) {
    int valid = 0;
    int visited[201] = {0};
    for(int i=0;i<numsSize;i++){
        if (visited[nums[i]+100]) continue;
        nums[valid++] = nums[i];
        visited[nums[i]+100] = 1;
    }
    return valid;
}