class Solution {
public:
    int minimumSubarrayLength(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = n + 1;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int tmp = 0;
                for (int k = i; k <= j; k++) {
                    tmp |= nums[k];
                }
                if (k <= tmp) {
                    ans = min(ans, j - i + 1);
                }
            }
        }
        if (ans == n+1) {
            ans = -1;
        }
        return ans;
    }
};