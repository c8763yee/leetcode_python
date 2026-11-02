struct llist_node {
    int key, val;
    struct llist_node *prev, *next;
};

typedef struct {
    struct llist_node *head, *tail;
    struct llist_node* map[10001];
    int len, capacity;
} LRUCache;

LRUCache* lRUCacheCreate(int capacity) {
    LRUCache* obj = malloc(sizeof(LRUCache));
    memset(obj->map, 0, 10001 * sizeof(struct llist_node*));
    obj->head = obj->tail = NULL;
    obj->capacity = capacity;
    obj->len = 0;
    return obj;
}
static void move_to_tail(LRUCache* obj, struct llist_node* node) {
    if (node == obj->tail)
        return;

    if (node->prev)
        node->prev->next = node->next;
    else
        obj->head = node->next;

    node->next->prev = node->prev;
    node->prev = obj->tail;
    node->next = NULL;
    obj->tail->next = node;
    obj->tail = node;
}
int lRUCacheGet(LRUCache* obj, int key) {
    if (obj->map[key] == NULL)
        return -1;

    move_to_tail(obj, obj->map[key]);
    return obj->map[key]->val;
}

void lRUCachePut(LRUCache* obj, int key, int value) {
    if (obj->map[key]) {
        obj->map[key]->val = value;
        move_to_tail(obj, obj->map[key]);
        return;
    }

    if (obj->len == obj->capacity) {
        struct llist_node* victim = obj->head;

        obj->map[victim->key] = NULL;
        obj->head = victim->next;

        if (obj->head)
            obj->head->prev = NULL;
        else
            obj->tail = NULL;

        free(victim);
        obj->len--;
    }
    struct llist_node* new_node = malloc(sizeof(struct llist_node));
    new_node->prev = obj->tail;
    new_node->next = NULL;
    new_node->key = key;
    new_node->val = value;

    obj->map[key] = new_node;
    if (obj->len == 0) {
        obj->head = obj->tail = new_node;
    } else {
        obj->tail->next = new_node;
        obj->tail = obj->tail->next;
    }
    obj->len++;
}

void lRUCacheFree(LRUCache* obj) {
    struct llist_node *cur = obj->head;

    while (cur) {
        struct llist_node *next = cur->next;
        free(cur);
        cur = next;
    }

    free(obj);
}

/**
 * Your LRUCache struct will be instantiated and called as such:
 * LRUCache* obj = lRUCacheCreate(capacity);
 * int param_1 = lRUCacheGet(obj, key);

 * lRUCachePut(obj, key, value);

 * lRUCacheFree(obj);
*/