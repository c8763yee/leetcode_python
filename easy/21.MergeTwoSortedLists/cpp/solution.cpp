/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (!list1){
            if(!list2) return nullptr;
            return list2;
        }else if (!list2) return list1;

        ListNode *root=nullptr, *ptr;

        int l1Val, l2Val, val;
        while (list1||list2){
            l1Val=list1?list1->val:-1337;
            l2Val=list2?list2->val:-1337;
            
            if (l2Val==-1337||l1Val<=l2Val && l1Val!=-1337){
                val = list1->val;
                list1 = list1->next;
            }
            else{
                val = list2->val;
                list2 = list2->next;
            }
            if (!root){
                root = new ListNode(val);
                ptr = root;
                continue;
            }else{
                ptr->next = new ListNode(val);
            }
            ptr = ptr->next; 
        }
        return root;
    }
};