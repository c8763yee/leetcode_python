static int dp[20] = {1, 1};

int generate(int lo, int hi)
{
    int size = hi - lo + 1;

    if (size <= 1)
        return 1;
    if (dp[size])
        return dp[size];

    int ret = 0;

    for (int i = lo; i <= hi; i++)
        ret += generate(lo, i - 1) *
               generate(i + 1, hi);

    return dp[size] = ret;
}

int numTrees(int n)
{
    return generate(1, n);
}