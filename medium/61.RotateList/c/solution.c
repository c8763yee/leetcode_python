/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (head == NULL || k == 0)
        return head;
    int count = 1;
    struct ListNode** indirect = NULL;
    struct ListNode* tail = head;
    for (tail = head; tail->next != NULL; tail = tail->next, count++)
        ;

    k %= count;
    if (k == 0)
        return head;

    indirect = &head;
    for (int i = 0; i < count - k; i++) {
        indirect = &((*indirect)->next);
    }
    tail->next = head;
    head = *indirect;
    *indirect = NULL;
    return head;
}