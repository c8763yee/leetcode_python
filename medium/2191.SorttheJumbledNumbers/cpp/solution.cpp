class Solution {
public:
    int key(int n) {
        if (n == 0)
            return this->mapping[0];
        int after = 0, factor = 1;

        while (n) {
            after += this->mapping[n % 10] * factor;
            factor *= 10;
            n /= 10;
        }
        return after;
    }

    vector<int> mapping;
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        this->mapping = mapping;
        std::sort(nums.begin(), nums.end(),
                  [this](int a, int b) { return this->key(a) < this->key(b); });

        return nums;
    }
};