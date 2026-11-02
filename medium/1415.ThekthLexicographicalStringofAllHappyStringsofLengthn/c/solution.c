void backtrack(int index, char** result, char* current, size_t resultSize,
               size_t currentSize, size_t* resultIndex, size_t currentIndex) {
    char happy[3] = "abc";

    if (index == currentSize) {
        current[currentSize] = '\0';  // 確保字串終止符
        result[*resultIndex] = strdup(current);  // 複製當前字串
        (*resultIndex)++;
        return;
    }

    for (int i = 0; i < 3; i++) {
        if (currentIndex > 0 && happy[i] == current[currentIndex - 1])
            continue;
        
        current[currentIndex] = happy[i];
        backtrack(index + 1, result, current, resultSize, currentSize, resultIndex, currentIndex + 1);
        current[currentIndex] = '\0';

    }
}

char* getHappyString(int n, int k) {
    size_t maxSize = 3 * (1 << (n - 1));
    if (k > maxSize)  // `k` 應該是 1-based index，所以用 `>` 而不是 `>=`
        return "";

    char** result = (char**)calloc(maxSize, sizeof(char*));
    char* current = (char*)calloc(n + 1, sizeof(char));  // 多一個字元給 '\0'
    size_t resultIndex = 0;

    backtrack(0, result, current, maxSize, n, &resultIndex, 0);

    char* happyString = strdup(result[k - 1]);  // 複製所需結果，避免 `free` 影響
    for (size_t i = 0; i < resultIndex; i++) {
        free(result[i]);  // 釋放已存的字串
    }
    free(current);
    free(result);

    return happyString;
}