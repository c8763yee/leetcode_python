/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* insertIntoBST(struct TreeNode* root, int val) {

    if (root == NULL)
        goto create_node;
    
    // all valid case: val < left, left < val < right, val > right
    if (val < root->val)
        root->left = insertIntoBST(root->left, val);
    else if (val > root->val)
        root->right = insertIntoBST(root->right, val);

    if (root) goto out;

create_node:
    struct TreeNode* new_node = malloc(sizeof(struct TreeNode));
    new_node->val = val;
    new_node->left = new_node->right = NULL;
    root = new_node;

out:
    return root;
}