

bool isPalindrome(int x){
    if (x<=0){return x==0;}
    else{
        int a=0,idx=(int)log10(x),y=x;
        while(x){
            a+=(x%10)*pow(10,idx--);
            x/=10;
        }return y==a;
    }
}

