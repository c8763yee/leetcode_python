/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void inorder(struct TreeNode* node, struct TreeNode** prev, int* min_diff) {
    if (!node)
        return;

    inorder(node->left, prev, min_diff);

    if (*prev && *min_diff > node->val - (*prev)->val)
        *min_diff = node->val - (*prev)->val;

    *prev = node;

    inorder(node->right, prev, min_diff);
}

int getMinimumDifference(struct TreeNode* root) {
    int min_diff = INT_MAX;
    struct TreeNode *prev = NULL;
    inorder(root, &prev, &min_diff);
    return min_diff;
}