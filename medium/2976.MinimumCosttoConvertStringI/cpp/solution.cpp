// optimization
#pragma GCC optimize("O3,unroll-loops")
auto init = []() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();

const unsigned int UNREACHABLE =
    INT_MAX >> 2; // prevent overflow when applying floyd warshall
class Solution {
public:
    long long minimumCost(string source, string target, vector<char>& original,
                          vector<char>& changed, vector<int>& cost) {

        // dp[src][dst]: cost of original to destination
        vector<vector<int>> dp(26, vector<int>(26, UNREACHABLE));
        char src, dst;

        size_t lstSize = original.size(), wordSize = source.size();
        for (int i = 0; i < lstSize; i++) {
            src = original[i] - 'a';
            dst = changed[i] - 'a';
            
            // dp[src][dst] = min(dp[src][dst], cost[i]);
            if (cost[i] < dp[src][dst])
                dp[src][dst] = cost[i];
        }

        // floyd warshall
        for (int k = 0; k < 26; k++) {
            dp[k][k] = 0;
            for (int i = 0; i < 26; i++) {
                for (int j = 0; j < 26; j++) {
                    if (dp[i][k] + dp[k][j] < dp[i][j])
                        dp[i][j] = dp[i][k] + dp[k][j];
                }
            }
        }

        // calculate path(cost to convert char), return -1 if unable to convert
        long long result = 0;
        for (int i = 0; i < wordSize; i++) {
            src = source[i] - 'a';
            dst = target[i] - 'a';
            if (dp[src][dst] == UNREACHABLE)
                return -1;
            result += dp[src][dst];
        }
        return result;
    }
};