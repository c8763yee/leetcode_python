bool isUpper(char c){
    return 65<=c&&c< 65+26;
}

bool isLower(char c){
    return 97<=c && c <97+26;
}

bool detectCapitalUse(char * word){
    int i=1;
    bool startWithUpper = isUpper(*word);
    bool startWithLower = isUpper(*word);
    bool containUpper=0, containLower=0;
    while (*(word+i)){
        bool isLetterUpper = isUpper(*(word+i++));
        if(startWithUpper){
            if (isLetterUpper){
                if (containLower) return 0;
                containUpper=1;
            }else{
                if (containUpper) return 0;
                containLower=1;
            }
        }else{
            if(isLetterUpper) return 0;
        }
    }
    return 1;
}