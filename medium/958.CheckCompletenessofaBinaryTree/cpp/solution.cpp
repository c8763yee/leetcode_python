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
    bool isCompleteTree(TreeNode* root) {
        std::vector<TreeNode*> q{root}, tmp;
        bool flag=false;
        while(!q.empty()){
            tmp.clear();
            for (TreeNode *node: q){
                if(!node){
                    flag = true;
                    continue;
                }
                if(flag) return false;
                tmp.push_back(node->left);
                tmp.push_back(node->right);
            }
            q = tmp;
        }
        return true;
    }
};