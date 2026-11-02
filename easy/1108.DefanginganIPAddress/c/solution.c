

char * defangIPaddr(char * address){
    int len = strlen(address), i=0, j=0;
    char *new = (char*)malloc(sizeof(char)*(22));
    for (i;address[i];i++){
        if(address[i] == '.'){
            new[j++] = '[';
            new[j++] = '.';
            new[j++] = ']';
        }
        else{
            new[j++] = address[i];
        }
    }
    new[j] = '\0';
    free(address);
    return new;
    
}