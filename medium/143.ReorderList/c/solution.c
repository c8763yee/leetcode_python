/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

bool recur(struct ListNode* back, struct ListNode** front) {
    if (!back)
        return true;

    if (!recur(back->next, front))
        return false;

    if (*front == back) {
        (*front)->next = NULL;
        return false;
    }

    if ((*front)->next == back) {
        back->next = NULL;
        return false;
    }

    struct ListNode* next = (*front)->next;
    (*front)->next = back;
    back->next = next;
    *front = next;

    return true;
}
void reorderList(struct ListNode* head) {
    struct ListNode** front = &head;
    recur(head, front);
}