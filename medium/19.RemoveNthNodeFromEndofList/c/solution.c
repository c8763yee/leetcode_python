/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode** ind = &head, *toBeFree;
    int cnt = 0;
    while (*ind) {
        ind = &(*ind)->next;
        cnt++;
    }
    ind = &head;
    for (int i = 0; i < cnt - n; i++) {
        ind = &(*ind)->next;
    }
    if (*ind){
        toBeFree = *ind;
        *ind = (*ind)->next;
        free(toBeFree);
        }
    return head;
}