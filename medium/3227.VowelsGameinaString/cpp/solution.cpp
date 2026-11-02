const bool ALICE = true, BOB = false;
const string VOWEL = "aeiou";
class Solution {
public:
    bool doesAliceWin(string s) {
        int count = 0;
        std::unordered_set<char> vowel(VOWEL.begin(), VOWEL.end());
        for (char c : s) {
            if (vowel.contains(c))
                count++;
        }
        return count == 0 ? BOB : ALICE;
    }
};