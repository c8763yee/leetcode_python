bool isSubsequence(char* s, char* t) {
    int ptr = 0;
    for (int i=0;t[i] && s[ptr];i++){
        if (t[i] == s[ptr]) ptr++;
    }

    return s[ptr] == 0;
}