class Solution {
public:
    int lengthOfLastWord(string s) {
        int last = s.size() - 1;
        while (last >= 0 && s[last] == ' ') last--;
        if (last < 0) return 0; // if the string is empty or contains only spaces
        int start = last;
        while (start >= 0 && s[start] != ' ') start--;
        return last - start;
    }
};