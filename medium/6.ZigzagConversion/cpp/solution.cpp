class Solution {
public:
    string convert(string s, int numRows) {
        if (s.size()<=1 || numRows <= 1)return s;
        std::vector<std::string> dp(numRows, "");
        int row = 0, step = 1;
        for (char c : s) {
            dp[row] += c;
            if (row == 0)
                step = 1;
            else if (row == numRows - 1)
                step = -1;

            row += step;
        }
        std::string result = "";
        for (std::string str : dp) {
            result += str;
        }
        return result;
    }
};
