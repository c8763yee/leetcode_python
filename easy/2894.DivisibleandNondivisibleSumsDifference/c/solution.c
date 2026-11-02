int differenceOfSums(int n, int m) {
    int num = ((1+n)*n)>>1;
    for (int i=m; i<=n; i+=m){
        num -= i<<1;
    }
    return num;
}