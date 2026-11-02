/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */

#define MX 100001
#pragma GCC optimize("03")
#pragma GCC target ("avx")

class Solution {
public:
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        std::unordered_set<int> childs;
        std::unordered_map<int, TreeNode*> tree;

        for (auto& vec : descriptions) {
            int value = vec[0];
            int child = vec[1];
            int direction = vec[2];

            if (!tree.contains(value)) {
                tree.insert({value, new TreeNode(value)});
            }

            if (!tree.contains(child)) {
                tree.insert({child, new TreeNode(child)});
            }
            if (direction)
                tree[value]->left = tree[child];
            else
                tree[value]->right = tree[child];

            childs.insert(child);
        }

        for (auto& [key, node] : tree) {
            if (!childs.contains(key))
                return node;
        }
        return NULL;
    }
};