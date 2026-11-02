#pragma GCC optimize("O3,unroll-loops")

auto x = []() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 0;
}();

class Solution {
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        const int INF = 10001;
        vector<vector<int>> dp(n, vector<int>(n, INF));

        for (int i = 0; i < n; ++i) {
            dp[i][i] = 0;
        }

        for (auto& ele : edges) {
            int src = ele[0], dst = ele[1], weight = ele[2];
            dp[src][dst] = dp[dst][src] = weight;
        }

        // Floyd-Warshall
        for (int k = 0; k < n; ++k) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
                }
            }
        }

        int maxCity = 0, minDistance = INF;
        for (int i = 0; i < n; ++i) {
            int count = 0;
            for (int j = 0; j < n; ++j) {
                if (i != j && dp[i][j] <= distanceThreshold) {
                    ++count;
                }
            }
            if (count <= minDistance) {
                minDistance = count;
                maxCity = i;
            }
        }

        return maxCity;
    }
};
