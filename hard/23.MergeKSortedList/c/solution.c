/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode *llist, **indirect = &llist, **node;
    for (; list1 && list2; *node = (*node)->next) {
        node = (list1->val < list2->val) ? &list1 : &list2;
        *indirect = *node;
        indirect = &(*indirect)->next;
    }

    *indirect = (struct ListNode*)((uintptr_t)list1 | (uintptr_t)list2);
    return llist;
}
struct ListNode* merge(struct ListNode **lists, int start, int end){
    if (end-start <= 0){
        return lists[start];
    }

    int mid = start+(end - start)/2;
    return mergeTwoLists(merge(lists, start, mid), merge(lists, mid+1, end));
}
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    if (listsSize==0) return NULL;
    return merge(lists, 0, listsSize-1);
}