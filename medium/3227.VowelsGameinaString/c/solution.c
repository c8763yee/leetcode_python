static inline bool isVowel(char *c) {
    return (*c == 'a' || *c == 'e' || *c == 'i' || *c == 'o' || *c == 'u');
}

bool doesAliceWin(char* s) {
    while(*s) {
        if (isVowel(s++)){
            return 1;
        }
    }
    return 0;
}