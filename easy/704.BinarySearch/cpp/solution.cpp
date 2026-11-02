class Solution {
public:
    int bs(vector<int> &nums, int left, int right, int target){
        if (left > right) return -1;
        if (left == right) return nums[left]==target?left:-1;
        int mid = (right-left)/2+left;
        if (nums[mid] < target) return bs(nums, mid+1, right, target);
        else if (nums[mid] > target) return bs(nums, left, mid - 1, target);
        return mid;

    }
    int search(vector<int>& nums, int target) {
        return bs(nums, 0, nums.size()-1, target);
    }
};