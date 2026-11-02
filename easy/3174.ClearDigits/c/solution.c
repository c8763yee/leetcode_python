char* clearDigits(char* s) {
    size_t index = 0;
    size_t sl = strlen(s);
    for (size_t i = 0; i<sl; i++) {
        if (s[i] >= '0' && s[i] <= '9')
            index -= 2;
        else
            s[index] = s[i];
        
        index++;
    }
    s[index] = '\0';
    return s;
}