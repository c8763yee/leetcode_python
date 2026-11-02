class Solution {
public:
    int minimumDeletions(string s) {
        vector<int> dp;
        uint32_t a_suffix = 0, b_prefix = 0;
        for(char c: s)
            a_suffix += (c == 'a');
        for(char c: s){
            if(c == 'a') a_suffix--;
            dp.push_back(a_suffix + b_prefix);
            if(c == 'b') b_prefix++;
        }

        int min_element = INT_MAX;

        for (int i: dp){
            if (min_element > i) min_element = i;
        }

        return min_element;
    }
};