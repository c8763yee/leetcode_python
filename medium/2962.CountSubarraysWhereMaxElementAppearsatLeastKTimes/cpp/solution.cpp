auto init = []()
{
    ios::sync_with_stdio(false);  
    cin.tie(nullptr);            
    cout.tie(nullptr);           
    return 'c';                  
}();

class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        long long n=nums.size();
        long long left = 0;
        long long cnt = 0;
        long long max_cnt = 0;
        long long max_ele = *max_element(nums.begin(), nums.end());
        for (long long right=0; right<n; right++){
            if (nums[right]==max_ele)max_cnt++;        
            while (left<=right && max_cnt>=k){
                if (nums[left++]==max_ele)max_cnt--;
            }
            cnt += (right - left + 1);
        }
        return ((1+n)*n/2)-cnt;
    }
};