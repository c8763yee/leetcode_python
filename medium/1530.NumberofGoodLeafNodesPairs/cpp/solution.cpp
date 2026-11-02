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

#pragma GCC optimize("O3,unroll-loops")
static const auto _ = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
}();
class Solution {
public:
    int count = 0;

    vector<int> dfsCountDistance(TreeNode* node, int distance) {
        if (!node)
            return {};
        if (!node->left && !node->right)
            return {0};

        vector<int> leftDistance = dfsCountDistance(node->left, distance);
        vector<int> rightDistance = dfsCountDistance(node->right, distance);

        for (int lDist : leftDistance) {
            for (int rDist : rightDistance) {
                if (lDist + rDist + 2 <= distance) {
                    count++;
                }
            }
        }

        vector<int> leafDistancesAfter;
        for (int lDist : leftDistance) {
            leafDistancesAfter.push_back(lDist + 1);
        }
        for (int rDist : rightDistance) {
            leafDistancesAfter.push_back(rDist + 1);
        }

        return leafDistancesAfter;
    }

    int countPairs(TreeNode* root, int distance) {
        dfsCountDistance(root, distance);
        return count;
    }
};
