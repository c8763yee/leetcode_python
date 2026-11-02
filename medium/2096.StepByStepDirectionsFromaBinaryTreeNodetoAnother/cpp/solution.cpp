/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr, right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, int p, int q) {
        if (!root || root->val == p || root->val == q)
            return root;
        TreeNode* leftNode = this->lowestCommonAncestor(root->left, p, q);
        TreeNode* rightNode = this->lowestCommonAncestor(root->right, p, q);
        if (leftNode && rightNode)
            return root;
        return leftNode ? leftNode : rightNode;
    }

    bool traversal(TreeNode* root, int target, string& path) {
        if (!root) return false;
        else if (root->val == target) return true;

        path.push_back('L');
        if (traversal(root->left, target, path)) return true;
        path.pop_back();

        path.push_back('R');
        if (traversal(root->right, target, path)) return true;
        path.pop_back();

        return false;
    }

    string getDirections(TreeNode* root, int startValue, int destValue) {
        // step 1. find LCA
        TreeNode* LCA = this->lowestCommonAncestor(root, startValue, destValue);

        // step 2. find path of LCA -> Start and LCA -> Dest
        string startPath = "", destPath = "";
        this->traversal(LCA, startValue, startPath);
        this->traversal(LCA, destValue, destPath);

        // step 3. find Longest common prefix of the two path, then remove it
        size_t commonLength = 0;
        while (commonLength < startPath.size() && commonLength < destPath.size() && startPath[commonLength] == destPath[commonLength]) {
            commonLength++;
        }
        string uniqueStartPath = startPath.substr(commonLength);
        string uniqueDestPath = destPath.substr(commonLength);

        string finalPath;
        finalPath.append(uniqueStartPath.size(), 'U');
        finalPath += uniqueDestPath;
        return finalPath;
    }
};