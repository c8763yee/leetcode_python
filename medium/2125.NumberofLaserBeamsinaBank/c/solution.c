int numberOfBeams(char** bank, int bankSize) {
    int prev = 0, total = 0, oneCount=0;
    for (int i = 0; i < bankSize; i++) {
        oneCount = 0;
        for(int j = 0;bank[i][j]!=0; j++){
            if(bank[i][j]=='1') oneCount++;
        }
        if (oneCount == 0)
            continue;
        if (prev != 0) {
            total += prev * oneCount;
        }
        prev = oneCount;
    }
    return total;
}