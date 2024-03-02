class Solution {
public:
    int countSubMultisets(vector<int>& nums, int l, int r) {
        // mx 表示 nums 里的最大值
        int mx = 0;
        // cnt[x] 表示大小为 x 的物品有几个
        unordered_map<int, int> cnt;
        for (int x : nums) mx = max(mx, x), cnt[x]++;
        // n 表示共有几种物品
        int n = cnt.size();

        const int MOD = 1e9 + 7;
        auto gao = [&](int LIM) {
            if (LIM < 0) return 0LL;

            // g[md] 是第 md 个滑动窗口的元素之和
            // 这里 g 的大小设为 mx + 1 是因为可能 mx == 0，c++ 不能开大小为 0 的数组
            long long f[n + 1][LIM + 1], g[mx + 1];
            memset(f, 0, sizeof(f));
            f[0][0] = 1;

            int i = 0;
            for (auto &p : cnt) if (p.first > 0) {
                i++;
                memset(g, 0, sizeof(long long) * p.first);
                for (int j = 0; j <= LIM; j++) {
                    // 当前需要使用哪个滑动窗口
                    int md = j % p.first;
                    // 滑动窗口滑动一步
                    g[md] = (g[md] + f[i - 1][j]) % MOD;
                    int t = j - p.first * (p.second + 1);
                    if (t >= 0) g[md] = (g[md] - f[i - 1][t] + MOD) % MOD;
                    // 把滑动窗口的值赋给 dp 数组
                    f[i][j] = g[md];
                }
            }

            // 加起来就是答案
            long long ret = 0;
            for (int j = 0; j <= LIM; j++) ret = (ret + f[i][j]) % MOD;
            return ret * (cnt[0] + 1) % MOD;
        };
        
        return (gao(r) - gao(l - 1) + MOD) % MOD;
    }
};