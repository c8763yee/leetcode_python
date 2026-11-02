
class Solution {
public:
    int maxOperations(string s) {
        int flag=2, one_count=0, ope=0;
        char prev = '\0';
        for (char c: s){
            if (prev && c != prev){
                flag--;
                if (flag==0){
                    flag = 2;
                    ope += one_count;
                }
            }
            if (c=='1')one_count++;
            prev = c;
        }
        if (flag == 1 && prev == '0') ope += one_count;
        return ope;
    }
};