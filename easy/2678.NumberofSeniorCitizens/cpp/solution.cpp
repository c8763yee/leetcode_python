class Solution {
public:
    int countSeniors(vector<string>& details) {
        int count = 0;
        for (string& detail : details){
            int year = std::stoi(detail.substr(11, 2));
            if (year>60) count++;
        }
        return count;
    }
};