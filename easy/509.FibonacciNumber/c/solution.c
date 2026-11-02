int arr[38];


int fib(int n){
    if (n<3){
        return n!=0;
    }for (int i=0;i<=3;i++){
    if (i<3) arr[i]=(i!=0);
}
    if(!arr[n]) arr[n]=fib(n-1)+fib(n-2);
    return arr[n];
}