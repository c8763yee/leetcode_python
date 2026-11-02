/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


int getDecimalValue(struct ListNode* head){
    struct ListNode* tmp = head;
    int total = 0;
    while(tmp){
        total*=2;
        total += tmp->val;
        tmp =tmp->next;
    }
    return total;
}