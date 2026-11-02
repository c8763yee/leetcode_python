#pragma GCC optimize("O3,unroll-loops")
static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root==NULL)
        {
            return 0;
        }
        
        int ans=max(maxDepth(root->left),maxDepth(root->right))+1;
        root->left=NULL;
        root->right=NULL;
        return ans;
    }
};