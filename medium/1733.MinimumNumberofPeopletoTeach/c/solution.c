bool findCommon(int **languages, int u, int v, int size_u, int size_v, int n) {
    int learned[n];
    memset(learned, 0, n * sizeof(int));
    for (int idx = 0; idx < size_u; idx++) {
        learned[languages[u][idx] - 1] = 1;
    }

    for (int idx = 0; idx < size_v; idx++) {
        if (learned[languages[v][idx] - 1]) {
           return true;
        }
    }
    return false;
}

int minimumTeachings(int n, int** languages, int languagesSize,
                     int* languagesColSize, int** friendships,
                     int friendshipsSize, int* friendshipsColSize) {

    int people = languagesSize;

    int u, v;
    bool noCommon[people];
    bool shouldEarlyReturn = true;

    memset(noCommon, false, people);
    for (int i = 0; i < friendshipsSize; i++) {
        // 1-indexed
        u = friendships[i][0] - 1;
        v = friendships[i][1] - 1;
        if (!findCommon(languages, u, v, languagesColSize[u], languagesColSize[v], n)){
            noCommon[u] = noCommon[v] = 1;
            shouldEarlyReturn = false;
        }
    }
    if (shouldEarlyReturn) return 0;

    int dp[languagesSize][n];
    memset(dp, 0, languagesSize * n * sizeof(int));
    for (int i = 0; i < languagesSize; i++) {
        if (noCommon[i] == 0)
            continue;
        for (int j = 0; j < languagesColSize[i]; j++) {
            dp[i][languages[i][j] - 1] = 1;
        }
    }

    int learnedBy = 0, maxLearnedBy = 0;
    for (int lang = 0; lang < n; lang++) {
        learnedBy = 0;
        for (int p = 0; p < people; p++) {
            learnedBy += (dp[p][lang] == 1 || !noCommon[p]);
        }
        if (learnedBy > maxLearnedBy) {
            maxLearnedBy = learnedBy;
        }
    }

    return people - maxLearnedBy;
}