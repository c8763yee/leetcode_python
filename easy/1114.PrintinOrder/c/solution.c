typedef struct {
    // User defined data may be declared here.
    // atomic_int owner;
    // or uses mutex

    int mutex[2];
} Foo;
// Function Declaration, do not remove
void printFirst(); // 00
void printSecond(); // 01
void printThird(); // 10

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    // Initialize user defined data here.
    memset(obj->mutex, 0, sizeof(int)*2);
    // assume `first` called first
    return obj;
}

void first(Foo* obj) {
    
    // printFirst() outputs "first". Do not change or remove this line.
    while(obj->mutex[0] || obj->mutex[1]);
    printFirst();
    obj->mutex[0] = 1;
}

void second(Foo* obj) {
    
    // printSecond() outputs "second". Do not change or remove this line.
    while(!(!obj->mutex[1] && obj->mutex[0]));
    printSecond();
    obj->mutex[0] = 0;
    obj->mutex[1] = 1;

}

void third(Foo* obj) {
    
    // printThird() outputs "third". Do not change or remove this line.
    while(!(obj->mutex[1] && !obj->mutex[0]));

    printThird();
    obj->mutex[1] = 0;
}

void fooFree(Foo* obj) {
    // User defined data may be cleaned up here.
    free(obj);
}