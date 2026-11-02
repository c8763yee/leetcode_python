class Solution {
public:
    int findTheWinner(int n, int k) {
        std::queue<int> q;
        int tmp;
        for (int i = 1; i <= n; i++) {
            q.push(i);
        }
        for (int i = 0; i < n - 1; i++) {
            // rotate left
            for (int j = 0; j < k - 1; j++) {
                tmp = q.front();
                q.pop();
                q.push(tmp);
            }
            q.pop();
        }
        return q.front();
    }
};