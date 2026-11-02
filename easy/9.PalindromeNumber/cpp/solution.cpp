class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0) return false;
        int sum= 0, idx = 1, curr = x, num, mod;
        while (x){
            num = x%10;
            x /= 10;
            if (idx++ == 9 && x){
                mod = curr%10;
                if (mod>3 || sum==214748364 && num>7){
                    return false;
                }
            }
            sum = sum * 10 + num;
        }return sum == curr;
    }
};