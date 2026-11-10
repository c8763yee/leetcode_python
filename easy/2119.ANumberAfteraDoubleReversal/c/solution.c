int reverse(int n){
    int ret = 0;
    while (n){
        ret = 10*ret + n%10;
        n/=10;
    }
    return ret;
}
bool isSameAfterReversals(int num) {
    return reverse(reverse(num))==num;
}