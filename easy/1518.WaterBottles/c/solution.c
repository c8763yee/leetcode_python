
// f(x, y, z) = x + f(y/z, y%z)
// x: numBottles
int f(int numBottles, int numExchange, int remain) {
    if (numBottles == 0 && (numBottles + remain) <numExchange)
        return 0;
    return (numBottles + f((numBottles + remain) / numExchange, numExchange,
                           (numBottles + remain) % numExchange));
}

int numWaterBottles(int numBottles, int numExchange) {
    if (numBottles == 0)
        return 0;
    return f(numBottles, numExchange, 0);
}