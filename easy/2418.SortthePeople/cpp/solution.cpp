#pragma GCC target("avx, mmx, sse2, sse3, sse4")
#pragma GCC optimize("O3,unroll-loops")
uint8_t disableSync = []() noexcept
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0U;
}();

class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {

        size_t size = names.size();
        std::vector<std::pair<int, int>> pairs;
        std::vector<std::string> result;

        // put index pair into pairs
        for (int i = 0; i < size; i++) {
            std::pair<int, int> currPair(i, heights[i]);
            pairs.push_back(currPair);
        }

        std::sort(pairs.begin(), pairs.end(), [](const auto& x, const auto& y) {
            return x.second > y.second;
        });

        for (const auto& [idx, pair]: pairs) {
            result.push_back(names[idx]);
        }
        return result;
    }
};