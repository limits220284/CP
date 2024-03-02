class Solution {
public:
    int maxValueOfCoins(vector<vector<int>>& piles, int k) {
        int n = piles.size();
        std::vector<std::vector<int>> pre(n, std::vector<int>());
        
        // 预处理前缀和
        for (int i = 0; i < n; ++i) {
            pre[i].push_back(0);
            for (int x : piles[i]) {
                pre[i].push_back(pre[i].back() + x);
            }
        }

        std::vector<std::vector<int>> f(n + 1, std::vector<int>(k + 1, 0));

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= k; ++j) {
                // 不选
                f[i][j] = f[i - 1][j];

                // 选
                for (int t = 1; t <= std::min(static_cast<int>(piles[i - 1].size()), j); ++t) {
                    f[i][j] = std::max(f[i][j], f[i - 1][j - t] + pre[i - 1][t]);
                }
            }
        }

        return f[n][k];
    }
};