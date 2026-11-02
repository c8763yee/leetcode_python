class Solution {
public:
    std::vector<char> storeStack(string s){
        std::vector<char> stack;
        for (char c: s){
            if (c!='#') {stack.push_back(c); continue;}
            if (!stack.empty()) stack.pop_back();   
        }return stack;
    }
    bool backspaceCompare(string s, string t) {
        return storeStack(s) == storeStack(t);
    }
};