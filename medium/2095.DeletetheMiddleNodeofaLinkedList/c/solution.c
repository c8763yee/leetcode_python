/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    struct ListNode *fast = head, **target = &head;
    while(fast && (fast)->next){
        fast = ((fast)->next->next);
        target = &((*target)->next);
    }

    *target = (*target)->next;
    return head;
}