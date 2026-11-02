int maxDepth(char * s){
    int idx = 0,max =0, len =0;
    for(idx;s[idx];idx++){
        if (s[idx] == '(')
        len++;
        else if (s[idx] == ')')
        len--;
        
        if (len>max){
            max=len;
        }
    }
    return max;
}