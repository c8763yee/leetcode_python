int reverse(int x){
    long sum=0, flag=(x<0);
    //x=abs(x);
    
    while (x){
        sum*=10;
        sum +=x%10;
        x/=10;
    }
    if(sum>2147483648||sum<-2147483648){
        return 0;
    }
    return sum;
}