
// unsigned int pow(unsigned int n, unsigned int x){
//     if (x == 0) return 1;
//     return pow(n*n, x/2) * pow(n*n, x/2) * x&1?n:1;
// }
int maximum69Number (int num) {
    int n = 1;
    int last_bit = -1;
    int bit = 0;
    while(n <= num){
        if ((num/n)%10 == 6){
            last_bit = bit;
        }
        n *= 10;
        bit++;
    }
    if (last_bit!= -1){
        num += 3*pow(10, last_bit);
    }
    return num;
}