char* maxSumOfSquares(int num, int sum) {
    if (num * 9 < sum)
        return "";
    char* numStr = calloc((num + 1),1);
    memset(numStr, '0', num);
    int temp = 0, i = 0;
    for (i = 0; i < num && sum > 0; i++) {
        temp = sum < 9 ? sum : 9;
        numStr[i] += temp;
        sum -= temp;
    }
    return numStr;
}