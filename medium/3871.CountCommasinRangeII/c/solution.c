long long countCommas(long long n) {
    long long count = 0;
    if (n >=1000){count += (n-999);}
    if (n >=1000000){count += (n-999999);}
    if (n >=1000000000){count += (n-999999999);}
    if (n >=1000000000000){count += (n-999999999999);}
    if (n >=1000000000000000){count += (n-999999999999999);}

    // long long threshold = 1000;

    // while(n >= threshold){
    //     count += (n-threshold+1);
    //     threshold *= 1000;
    // }

    return count;
}

/*  0       K       M       G       T
    |       |                               (n comma)
    |       |       |                       (n-1 comma)
    |       |       |       |               (n-2 comma)
    |       |       |       |       |       (n-3 comma)
*/ 