class Solution {
public:
    int minimumPushes(string word) {
        int dp[26] = {0};
        for (const char c : word){
            dp[c-'a']++;
        }
        std::sort(dp, dp+26, std::greater<int>());
        int result = 0;
        uint8_t index = 8;
        for (int i=0;i<26;i++){
            if (!dp[i]) continue;
            result += ((index++/8) * dp[i]);
        }
        return result;

    }
};