class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* first = head;
        for(int i=0;i<n;i++)
            first=first->next;
        
        if(!first)
            return head->next;
        
        ListNode* second = head;
        for(;first->next;first=first->next)
            second=second->next;
        
        if(second->next)
            second->next=second->next->next;
        
        return head;
    }
};