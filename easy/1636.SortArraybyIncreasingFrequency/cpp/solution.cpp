class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        std::unordered_map<int, int> counter;
        std::vector<std::pair<int, int>> vec;
        for (int i : nums) {
            counter[i]++;
        }
        for (auto& [key, value] : counter) {
            vec.push_back(std::pair<int, int>(key, value));
        }
        std::sort(vec.begin(), vec.end(), [](auto& a, auto& b) {
            if (a.second != b.second)
                return a.second < b.second;
            else
                return a.first > b.first;
        });
        int index = 0;
        for (auto& [key, count] : vec) {
            for (int i = 0; i < count; i++) {
                nums[index + i] = key;
            }
            index += count;
        }
        return nums;
    }
};