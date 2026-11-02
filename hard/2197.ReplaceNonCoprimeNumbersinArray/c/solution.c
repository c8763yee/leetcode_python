/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
int lcm(int a, int b) {
    int g = gcd(a, b);
    return (a / g) * (b / g) * g;
}
int* replaceNonCoprimes(int* nums, int numsSize, int* returnSize) {
    int stack_idx = 0, stack_top = 0, cur = 0;
    for(int i=0;i<numsSize;i++){
        cur = nums[i];
        while(stack_idx && gcd(nums[stack_idx-1], cur) > 1){
            stack_top = nums[--stack_idx];
            cur = lcm(stack_top, cur);
        }
        nums[stack_idx++] = cur;
    }
    *returnSize = stack_idx;
    return nums;
}