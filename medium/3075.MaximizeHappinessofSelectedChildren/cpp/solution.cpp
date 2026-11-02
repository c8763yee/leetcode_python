class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        long long c;
        long long result = 0;
        std::sort(happiness.begin(), happiness.end());
        for (int i=0;i<k;i++){
            c = happiness.back() - i;
            happiness.pop_back();
            if (c<0) break;
            result += c;
        }
        return result;
    }
};