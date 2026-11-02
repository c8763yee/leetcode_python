class Solution {
public:
    int minChanges(int n, int k) {
        if (k>n) return -1;
        int count = 0;
        while (n){
            if (!(n&1)&&k&1)return -1;
            else if (n&1 && !(k&1)){
                count++;
            }

            n >>= 1;
            k >>= 1;
        }
        return count;
    }
};