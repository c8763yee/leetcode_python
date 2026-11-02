class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> maps;
        int i = 0;
        for (int e : nums){
            if (maps.contains(target-e)) return {i, maps[target-e]};
            maps[e] = i;
            i++;
        }
            
        return {};
    }
};