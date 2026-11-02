int max(int a, int b) {
    return a > b ? a : b;
}

// 回傳節點高度；若子樹已經失衡，則回傳 -1 作為「失衡訊號」
int checkHeight(struct TreeNode* node) {
    if (node == NULL)
        return 0;

    // 1. 先往下檢查左子樹，若發現左子樹已失衡 (-1)，直接往上回報 -1
    int left = checkHeight(node->left);
    if (left == -1) return -1;

    // 2. 再檢查右子樹，若發現右子樹已失衡 (-1)，直接往上回報 -1
    int right = checkHeight(node->right);
    if (right == -1) return -1;

    // 3. 若當前節點的左右子樹高度差 > 1，代表在這一層失衡了，回傳 -1
    if (abs(left - right) > 1)
        return -1;

    // 4. 若都平衡，正常回傳當前節點的真實高度
    return max(left, right) + 1;
}

bool isBalanced(struct TreeNode* root) {
    // 只要最終回傳值不是 -1，就代表整棵樹處處平衡
    return checkHeight(root) != -1;
}