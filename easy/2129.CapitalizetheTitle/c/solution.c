char * capitalizeTitle(char * title){
    int start = 0, space = 0, i=0, A=65, Z=90, a=97, z=a+25;
    do{
        if (*(title+i) == ' ' || *(title+i) == '\0'){
            space = i;
            // convert first letter to upper
            int toosmall = (space-start)>2;
            if (*(title+start)>=a){
                *(title+start)-= 32;
            }
            for(int j=start+toosmall ; j<space; j++){
                if (*(title+j)>=A && *(title+j)<=Z){
                    *(title+j) += 32;
                }
            }
            start = space+1;
        }
    }while(*(title+i++));
    return title;
}