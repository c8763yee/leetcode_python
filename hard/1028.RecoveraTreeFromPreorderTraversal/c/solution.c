/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int parse_num(char** c) {
    int n = 0;

    while (**c >= '0' && **c <= '9') {
        n = n * 10 + (**c - '0');
        (*c)++;
    }

    return n;
}
struct Stack {
    int index, capacity;
    struct TreeNode** stack;
};

struct Stack* new_stack(int capacity) {
    struct Stack* stack = calloc(1, sizeof(struct Stack));
    stack->stack = malloc(sizeof(struct TreeNode*) * capacity);
    stack->capacity = capacity;
    return stack;
}

struct TreeNode* new_node(int value, struct TreeNode* left,
                          struct TreeNode* right) {
    struct TreeNode* node = malloc(sizeof(struct TreeNode));
    node->val = value;
    node->left = left;
    node->right = right;
    return node;
}

void push(struct Stack* obj, struct TreeNode* node) {
    if (obj->index == obj->capacity)
        return;
    obj->stack[obj->index++] = node;
}
struct TreeNode* pop(struct Stack* obj) {
    if (obj->index == 0)
        return NULL;
    struct TreeNode* ret = obj->stack[obj->index - 1];
    obj->stack[--obj->index] = NULL;
    return ret;
}

struct TreeNode* recoverFromPreorder(char* traversal) {
    size_t n = strlen(traversal);
    int level, value, last_level;
    struct TreeNode *head = NULL, *node, *top;
    struct Stack* stack = new_stack(n);

    // parse number and node
    for (char* c = traversal; *c;) {
        level = 0;

        while (*c == '-') {
            level++;
            c++;
        }

        value = parse_num(&c);
        node = new_node(value, NULL, NULL);
        if (level == 0) {
            head = node;
            goto next;
        }

        // compare diff between last level and current level
        int d = level - last_level;
        while (d <= 0) {
            pop(stack);
            d++;
        }
        top = stack->stack[stack->index - 1];
        if (top->left==NULL)
            top->left = node;
        else
            top->right = node;

    next:
        push(stack, node);
        last_level = level;
    }
    free(stack->stack);
    free(stack);
    return head;
}