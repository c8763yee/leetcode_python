/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* mergeInBetween(struct ListNode* list1, int a, int b,
                                struct ListNode* list2) {
    struct ListNode **p = &list1;

    for (int i = 0; i < a; i++)
        p = &(*p)->next;

    struct ListNode *after = *p;
    for (int i = a; i <= b; i++)
        after = after->next;

    *p = list2;
    while (*p)
        p = &(*p)->next;

    *p = after;
    return list1;
}