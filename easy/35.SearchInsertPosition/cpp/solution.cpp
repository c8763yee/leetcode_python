class Solution {
public:
    /*int binarySearch(vector<int> &nums, int left, int right, int target){
        int mid = left + (right - left) / 2;
        if (right < left) return left;
        if (nums[mid] == target){
            return mid;
        }
        if (nums[mid] > target){
            return binarySearch(nums, left, mid-1, target);
        }

        return binarySearch(nums, mid+1, right, target);
    }*/

    int searchInsert(vector<int>& nums, int target) {
        int  left = 0, right = nums.size() - 1, mid;
        while (left <= right){
            mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] > target) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    }
};