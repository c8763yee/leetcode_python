/**
 * Definition for singly-linked list.
 * struct ListNode {
 * int val;
 * struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    // pp 是一個「指標的指標」，它初始時指向 head 指標本身。
    // 這允許我們在必要時直接修改 head。
    struct ListNode **pp = &head;
    
    // 當 *pp (即當前節點) 不是 NULL 時，繼續迴圈。
    while (*pp != NULL) {
        struct ListNode *current = *pp;
        
        // 檢查當前節點是否為一個重複序列的開始
        // 條件：下一個節點存在，且值與當前節點相同
        if (current->next != NULL && current->val == current->next->val) {
            int val_to_remove = current->val;
            
            // 進入內部迴圈，跳過所有值為 val_to_remove 的節點
            // 關鍵操作：*pp = (*pp)->next;
            // 這個操作會修改它所指向的指標 (可能是 head 或某個 prev->next)，
            // 讓它指向下一個節點，從而「刪除」當前的 *pp 節點。
            while (*pp != NULL && (*pp)->val == val_to_remove) {
                // 如果需要手動釋放記憶體，可以在這裡做
                // struct ListNode *temp = *pp;
                *pp = (*pp)->next;
                // free(temp);
            }
        } else {
            // 如果當前節點不是重複的，我們就保留它。
            // 將 pp 指向當前節點的 next 指標的位址，準備檢查下一個節點。
            pp = &(*pp)->next;
        }
    }
    
    return head;
}