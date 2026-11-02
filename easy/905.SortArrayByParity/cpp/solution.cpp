class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        // swap when leftPtr is odd and rightPtr is even
        int left = 0, right = nums.size()-1, tmp;
        while (left < right){
            if (nums[left]%2 && !(nums[right]%2)) 
            {
                tmp = nums[left];
                nums[left] = nums[right];
                nums[right] = tmp;
            }if (!(nums[left]%2)) left++;
            if (nums[right]%2) right--;
        }return nums;
    }
};