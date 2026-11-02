/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> result;
    TreeNode* dfs(TreeNode *node, const std::unordered_set<int>& nodeToDelete, bool isRoot){
        if (!node)return nullptr;
        bool willDelete = nodeToDelete.contains(node->val);
        if (isRoot&&!willDelete)this->result.push_back(node);

        node->left = this->dfs(node->left, nodeToDelete, willDelete);
        node->right = this->dfs(node->right, nodeToDelete, willDelete);

        return willDelete?nullptr:node;
    }
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        const std::unordered_set<int> nodeToDelete(to_delete.begin(), to_delete.end());
        this->dfs(root, nodeToDelete, true);
        return this->result;
    }
};