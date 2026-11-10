int pivotInteger(int n) {
    int right = (1 + n) * n / 2, left = 0;
    for (int i = 1; i <= n; i++) {
        left += i;
        if (left == right)
            return i;
        right -= i;
    }

    return -1;
}