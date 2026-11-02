/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* searchBST(struct TreeNode* root, int val) {
    if (!root || root->val == val) return root;

    return (struct TreeNode *)((uintptr_t)searchBST(root->left, val) | (uintptr_t)searchBST(root->right, val));
}