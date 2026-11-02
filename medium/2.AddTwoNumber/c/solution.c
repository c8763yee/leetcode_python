/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* newNode(int val){
    struct ListNode* node = (struct ListNode *)calloc(1, sizeof(struct ListNode));
    node->val = val;
    return node;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    bool carry = 0;
    int sumVal, l1val, l2val;
    struct ListNode* head =newNode(0);
    struct ListNode* curr = head;
    while (l1 || l2 || carry) {
        l1val = l1 ? l1->val : 0;
        l2val = l2 ? l2->val : 0;

        sumVal = l1val + l2val + carry;
        carry = sumVal / 10;

        curr->next = newNode(sumVal%10);
        curr = curr->next;

        l1 = l1 ? l1->next : NULL;
        l2 = l2 ? l2->next : NULL;
    }
    return head->next;
}