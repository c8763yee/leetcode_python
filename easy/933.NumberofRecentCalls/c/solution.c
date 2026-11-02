typedef struct {
    int q[10000]; // store valid t (which within range)
    int head, tail;
} RecentCounter;

RecentCounter* recentCounterCreate() {
    RecentCounter* counter = malloc(sizeof(RecentCounter));
    counter->head = counter->tail = 0;
    return counter;
}

int recentCounterPing(RecentCounter* obj, int t) {
    obj->q[obj->head++] = t; // t must be largest ping
    while (obj->tail != obj->head && obj->q[obj->tail] < t-3000) {
        obj->tail++;
    }
    return (obj->head - obj->tail);
}

void recentCounterFree(RecentCounter* obj) { free(obj); }

/**
 * Your RecentCounter struct will be instantiated and called as such:
 * RecentCounter* obj = recentCounterCreate();
 * int param_1 = recentCounterPing(obj, t);

 * recentCounterFree(obj);
*/