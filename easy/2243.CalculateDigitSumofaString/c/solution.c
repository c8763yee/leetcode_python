
char* digitSum(char* s, int k) {
    int n = strlen(s);
    char* stack = malloc(n + 1);
    if (!stack) return NULL;

    memcpy(stack, s, n + 1);

    while (n > k) {
        int ptr_w = 0;

        for (int i = 0; i < n; i += k) {
            int tmp = 0;

            for (int j = 0; j < k && i + j < n; j++) {
                tmp += stack[i + j] - '0';
            }

            char digits[12];
            int len = snprintf(digits, sizeof(digits),
                               "%d", tmp);

            memcpy(stack + ptr_w, digits, len);
            ptr_w += len;
        }

        n = ptr_w;
        stack[n] = '\0';
    }

    return stack;
}
