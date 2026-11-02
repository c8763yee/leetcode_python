class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int total = 0, idx = 0, leftSum = 0;
        for (int i: nums) total += i;
        for (int i: nums){
            total -= i;
            if (total == leftSum) return idx;
            leftSum += i;
            idx++;
        }
        return -1;
    }
};