/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* partition(struct ListNode* head, int x) {
    if (head == NULL || head->next == NULL)
        return head;

    struct ListNode *less = calloc(1, sizeof(struct ListNode)),
                    *more = calloc(1, sizeof(struct ListNode));

    struct ListNode *lessTail = less, *moreTail = more;
    for (struct ListNode* temp = head; temp != NULL; temp = temp->next) {
        if (temp->val < x) {
            lessTail->next = temp;
            lessTail = lessTail->next;
        } else {
            moreTail->next = temp;
            moreTail = moreTail->next;
        }
    }
    // X 1 2 2
    // X 4 3 5
    more = more->next;
    lessTail->next = more;
    moreTail->next = NULL;
    return less->next;
}