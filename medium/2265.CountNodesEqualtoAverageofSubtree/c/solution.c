int averageOfSubtree(struct TreeNode* root)
{
    if (!root)
        return 0;

    int orig_val = root->val;
    int matched = 0;

    matched += averageOfSubtree(root->left);
    matched += averageOfSubtree(root->right);

    root->val = (orig_val << 10) | 1;

    if (root->left)
        root->val += root->left->val;

    if (root->right)
        root->val += root->right->val;

    int sum = root->val >> 10;
    int count = root->val & 0x3ff;

    return matched + (sum / count == orig_val);
}