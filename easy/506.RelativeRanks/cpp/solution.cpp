class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        std::map<int, int> mp1;
        int size = score.size(), i;
        // set mapping for element and index
        for (i=0;i<size;i++)
            mp1[score[i]] = i;
        std::sort(score.begin(), score.end(), std::greater<int>());
        std::vector<string> result(score.size());
        for(i=0;i<size;i++){
           if (i == 0) {
                result[mp1[score[i]]] = "Gold Medal";
            } else if (i == 1) {
                result[mp1[score[i]]] = "Silver Medal";
            } else if (i == 2) {
                result[mp1[score[i]]] = "Bronze Medal";
            } else {
                result[mp1[score[i]]] = to_string(i + 1);
            }
        }
        return result;        
    }
};