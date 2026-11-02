int canBeTypedWords(char* text, char* brokenLetters) {
    bool brkLetinKbd[26];
    for (char i = 0; brokenLetters[i]; i++) {
        brkLetinKbd[brokenLetters[i] - 'a'] = true;
    }

    bool skipWord = false;
    short canType = 0;
    for (short i = 0; text[i]; i++) {
        if (text[i] == ' ') {
            canType += (skipWord == false);
            skipWord = false;
            continue;
        }
        else if (skipWord) {
            continue;
        }

        if (brkLetinKbd[text[i] - 'a']) {
            skipWord = true;
            continue;
        }
    }
    return canType + (skipWord == false);
}