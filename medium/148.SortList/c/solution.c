/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* merge(struct ListNode *a, struct ListNode *b){
    struct ListNode *ret = NULL, **ind = &ret, **tmp;
    while (a && b){
        tmp = a->val <= b->val ? &a : &b;
        *ind = *tmp;
        
        *tmp = (*tmp)->next;
        ind = &(*ind)->next;
    }

    *ind = a?a:b;
    return ret;
}

struct ListNode* sortList(struct ListNode* head) {
    if (!head || !head->next) return head;

    // find middle node 
    struct ListNode* fast = head, **mid = &head;
    while(fast &&fast->next){
        fast = fast->next->next;
        mid = &(*mid)->next;
    }

    // reuse fast
    fast = *mid;
    *mid = NULL;

    return merge(sortList(head), sortList(fast));
}