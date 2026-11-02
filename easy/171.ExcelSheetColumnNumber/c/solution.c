

int titleToNumber(char * columnTitle){
    int sum=0;
    while (*columnTitle){
        sum *=26;
        sum += *(columnTitle++)-'A'+1;
    }
    return sum;
}