class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int length = nums.size();
        int left = 0, right = length - 1;
        int ans;
        if (length == 1)return nums[0];
        while(left<=right){
            int mid = left + (right - left) / 2;
            int idx = mid * 2;
            if (idx == length || nums[idx] != nums[idx + 1]){
                right = mid - 1;
                ans = nums[idx];
            }else{
                left = mid + 1;
            }
        }
        return ans;
    }
};