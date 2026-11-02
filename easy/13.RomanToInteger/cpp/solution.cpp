class Solution {
public:
    int romanToInt(string s) {
    string Symbol = "IVXLCDM";
    std::vector<int> Value = {1,5,10,50,100,500,1000};
    std::map<char, int> Map;
    
    for(int i=0;i<7;i++){
        Map.insert({Symbol[i], Value[i]});
    }
    
    int curr, next, sum = 0;
    for(int i=0; i<s.size();i++)
    {
        curr = Map[s[i]];
        next = Map[s[i+1]];
        sum += (-2*(curr < next) + 1) * curr;
    }
    return sum;
    }
};