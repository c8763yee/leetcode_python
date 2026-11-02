/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* insert(int *nums, int lo, int hi){
    if (lo > hi) return NULL;
    int mid = (lo + hi) >> 1;
    struct TreeNode *node = malloc(sizeof(struct TreeNode));
    node->val = nums[mid];
    node->left = insert(nums, lo, mid-1);
    node->right = insert(nums, mid+1, hi);
    return node;

}
struct TreeNode* sortedArrayToBST(int* nums, int n) {
    
    return insert(nums, 0, n-1);
}