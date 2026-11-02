int tribonacci(int n){
    if (n<3) return n > 0;
    int a=0, b=1, c=1, tmp, i;
    for (i=3; i<=n; i++){
        tmp = c;
        c = a + b + tmp;
        a = b;
        b = tmp;
    }
    return c;
}