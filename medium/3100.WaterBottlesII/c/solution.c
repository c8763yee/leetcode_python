int maxBottlesDrunk(int numBottles, int numExchange) {
    int empty = 0;
    int total = 0;
    while (numBottles + empty >= numExchange){
        total += numBottles;
        empty += (numBottles-numExchange);
        numBottles = 0;
        numBottles++;
        numExchange++;
    }
    // printf("Final: numBottles: %d, empty: %d\n", numBottles, empty);
    return total + numBottles;
}