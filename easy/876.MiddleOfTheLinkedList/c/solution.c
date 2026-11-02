/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* middleNode(struct ListNode* head){
    int cnt = 0, middle;
    struct ListNode* tmp = head;
    while(tmp){
        cnt++;
        tmp = tmp->next;
    }
    middle = cnt/2;
    for(int i=0;i<middle;i++){
        head = head->next;
    }
    free(tmp);
    return head;
}