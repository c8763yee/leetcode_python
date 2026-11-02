#include<stdio.h>

int lengthOfLastWord(char* s) {
    int last = strlen(s) - 1;
    int start;
    for (last; last >=0 && *(s+last) == ' '; last--);
    for (start=last; start >=0 && *(s+start) != ' '; start--);
    return last - start;
}