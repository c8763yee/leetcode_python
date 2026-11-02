int scoreOfParentheses(char* s) {
    int arr[51] = {0}, val, ptr = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == '(') {
            arr[ptr++] = -1;
            continue;
        }
        
        val = 0;
        while (ptr && arr[ptr - 1] != -1)
            val += arr[--ptr];

        arr[ptr - 1] = val == 0 ? 1 : val << 1;
    }
    int ret = 0;
    for(int i=0;i<ptr;i++){
        ret += arr[i];
    }
    return ret;
}