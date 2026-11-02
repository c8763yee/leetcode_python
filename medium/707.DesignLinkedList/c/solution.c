
typedef struct list_item {
    int val;
    struct list_item* next;
} list_item_t;

typedef struct {
    list_item_t* head;
    int size;
} MyLinkedList;

list_item_t* create_list_item(int val) {
    list_item_t* node = (list_item_t*)calloc(1, sizeof(list_item_t));
    node->val = val;
    return node;
}

list_item_t** traversal(list_item_t** head, int index) {
    list_item_t** indirect = head;
    int i = 0;
    for (i = 0; i < index; i++, indirect = &(*indirect)->next) {
    }
    return indirect;
}

MyLinkedList* myLinkedListCreate() {
    MyLinkedList* obj = (MyLinkedList*)calloc(1, sizeof(MyLinkedList));
    return obj;
}

int myLinkedListGet(MyLinkedList* obj, int index) {
    if (index > obj->size) return -1;

    list_item_t** node = traversal(&(obj->head), index);
    return (*node) ? (*node)->val : -1;
}

void myLinkedListAddAtHead(MyLinkedList* obj, int val) {
    list_item_t **head = &(obj->head), *new_node = create_list_item(val);

    new_node->next = *head;
    obj->head = new_node;
    obj->size++;
}

void myLinkedListAddAtTail(MyLinkedList* obj, int val) {
    list_item_t** indirect = &(obj->head);
    while (*indirect)
        indirect = &(*indirect)->next;
    *indirect = create_list_item(val);
    obj->size++;
}

void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val) {
    if (index > obj->size) return;

    list_item_t *new_node = create_list_item(val),
                **target = traversal(&(obj->head), index);


    new_node->next = *target;
    *target = new_node;
    obj->size++;
}

void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index) {
    if (index >= obj->size) return;

    list_item_t** target = traversal(&(obj->head), index);
    *target = (*target)->next;
    obj->size--;
}

void myLinkedListFree(MyLinkedList* obj) {
    while (obj->head) {
        list_item_t* node = obj->head;
        obj->head = obj->head->next;
        free(node);
    }
    free(obj);
}

/**
 * Your MyLinkedList struct will be instantiated and called as such:
 * MyLinkedList* obj = myLinkedListCreate();
 * int param_1 = myLinkedListGet(obj, index);

 * myLinkedListAddAtHead(obj, val);

 * myLinkedListAddAtTail(obj, val);

 * myLinkedListAddAtIndex(obj, index, val);

 * myLinkedListDeleteAtIndex(obj, index);

 * myLinkedListFree(obj);
*/