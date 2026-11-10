
bool symmertic(struct TreeNode* a, struct TreeNode* b){
    if (!(a&&b)) return !(a || b);
    return  a->val == b->val && symmertic(a->left, b->right) && symmertic(a->right, b->left);
}

bool isSymmetric(struct TreeNode* root) {
    if (root == NULL)
        return true;
    return symmertic(root->left, root->right);
}