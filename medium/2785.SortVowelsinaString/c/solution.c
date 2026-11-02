#pragma GCC optimize("O3,flto,ffast,math,march=native,mtune = native")

bool isVowel(char c) {
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
}

// int cmp(const void *a,const void *b){
//     if (*(int *)a&1<<25){
//         return 1;
//     }
// }

int cmpChar(const void* a, const void* b) {
    return (*((char*)a) - *((char*)b));
}
char* sortVowels(char* s) {
    // XXXX XX X X XXXX XXXX XXXX XXXX XXXX XXXX
    //        |v|         index       |   char  |

    int l = strlen(s), vowelIndex = 0;
    char vowel[l];

    memset(vowel, 0, l);
    for (int i = 0; i < l; i++) {
        if (isVowel(s[i])) {
            vowel[vowelIndex++] = s[i];
        }
    }
    qsort(vowel, vowelIndex, 1, cmpChar);

    vowelIndex = 0;
    for (int i = 0; i < l; i++) {
        if (isVowel(s[i])) {
            s[i] = vowel[vowelIndex++];
        }
    }
    return s;
}