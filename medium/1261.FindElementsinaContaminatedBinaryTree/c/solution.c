/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

typedef struct {
    struct TreeNode* root;
} FindElements;

void recover(struct TreeNode* root) {
    if (root == NULL)
        return;
    if (root->left) {
        root->left->val = root->val * 2 + 1;
        recover(root->left);
    }
    if (root->right) {
        root->right->val = root->val * 2 + 2;
        recover(root->right);
    }
}

FindElements* findElementsCreate(struct TreeNode* root) {
    root->val = 0;
    recover(root);
    FindElements* element = (FindElements*) malloc(sizeof(FindElements));
    element->root = root;
    return element;
}

bool treeNodeFind(struct TreeNode* root, int target) {
    if (root == NULL)
        return false;
    if (root->val == target)
        return true;
    return treeNodeFind(root->left, target) ||
           treeNodeFind(root->right, target);
}
bool findElementsFind(FindElements* obj, int target) {
    return treeNodeFind(obj->root, target);
}
void findElementsFree(FindElements* obj) {
    free(obj->root);
    free(obj);
}

/**
 * Your FindElements struct will be instantiated and called as such:
 * FindElements* obj = findElementsCreate(root);
 * bool param_1 = findElementsFind(obj, target);

 * findElementsFree(obj);
*/