void reverseChar(char* word, int word_end);

char* reversePrefix(char* word, char ch) {
    for (int i=0; word[i] != '\0'; i++){
        if (word[i] == ch)
        {
            reverseChar(word, i);
            break;
        }
    }
    return word;
}

void reverseChar(char* word, int word_end){
    int left = 0;
    int right = word_end;
    char t;
    while (left < right){
        t = word[left];
        word[left++] = word[right];
        word[right--] = t;
    }
}
