int trailingZeroes(int n) {
    // how many 2 and 5 in n
    int d = 5, val = 0;
    while (d <= n){
        val += n/d;
        d *= 5;
    }return val;
}