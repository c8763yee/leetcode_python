typedef struct {
    int* product;
    size_t size;
    size_t capacity;
} ProductOfNumbers;

ProductOfNumbers* productOfNumbersCreate() {
    ProductOfNumbers* product =
        (ProductOfNumbers*)malloc(sizeof(ProductOfNumbers));

    product->size = 0;
    product->capacity = 1;
    product->product = (int*)calloc(product->capacity, sizeof(int));
    product->product[0] = 1;
    return product;
}

void productOfNumbersAdd(ProductOfNumbers* obj, int num) {
    if (obj->size + 1 == obj->capacity) {
        obj->capacity <<= 1;
        obj->product = (int*)realloc(obj->product, obj->capacity * sizeof(int));
    }

    if (num == 0) {
        obj->size = 0;
        obj->product[0] = 1;
    } else {
        obj->product[obj->size + 1] = obj->product[obj->size] * num;
        obj->size++;
    }
}

int productOfNumbersGetProduct(ProductOfNumbers* obj, int k) {
    if (k > obj->size) {
        return 0;
    }
    return obj->product[obj->size] / obj->product[obj->size - k];
}

void productOfNumbersFree(ProductOfNumbers* obj) {
    free(obj->product);
    free(obj);
}

/**
 * Your ProductOfNumbers struct will be instantiated and called as such:
 * ProductOfNumbers* obj = productOfNumbersCreate();
 * productOfNumbersAdd(obj, num);

 * int param_2 = productOfNumbersGetProduct(obj, k);

 * productOfNumbersFree(obj);
*/