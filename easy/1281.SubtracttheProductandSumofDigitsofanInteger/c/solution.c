int subtractProductAndSum(int n){
    int p=1,s=0,r;
    while (n){
        r=n%10;
        p*=r;
        s+=r;
        n/=10;
    }
    return p-s;
}