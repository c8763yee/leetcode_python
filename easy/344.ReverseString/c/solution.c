void reverseString(char* s, int sSize){
    int i=0, j=sSize - 1;
    while(i < j){
        s[i++]^=s[j--]^=s[i]^=s[j];
    }return s;
}