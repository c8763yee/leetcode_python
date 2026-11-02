int* distributeCandies(int candies, int num_people, int* returnSize){
    *returnSize=num_people;
    int idx=0,*people = malloc(sizeof(int)*num_people);
    for (int i = 0; i < num_people; i++)
    {
        people[i]=0;
    }
    
    while (candies){
        if (idx<candies){
            people[idx%num_people] += idx+1;
        }else{
            people[idx%num_people] +=candies;
            break;
        }
        candies -= (idx++ + 1);

    }
    return people;
}