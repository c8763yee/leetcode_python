class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        ListNode *fast = head, **slow = &head;
        while (fast && fast->next){
            fast = fast->next->next;
            slow = &(*slow)->next;
        }
        *slow = (*slow)->next;
        return head;
    }
};