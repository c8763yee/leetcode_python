/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int node_cmp(struct ListNode *a, struct ListNode *b){
    return a->val - b->val;
}
struct ListNode* mergeTwoLists(struct ListNode* a, struct ListNode* b) {
     struct ListNode *ret = NULL, **ind = &ret, **tmp;
    while (a && b){
        tmp = node_cmp(a, b) < 0 ? &a : &b;
        *ind = *tmp;
        
        *tmp = (*tmp)->next;
        ind = &(*ind)->next;
    }

    *ind = a?a:b;
    return ret;
}