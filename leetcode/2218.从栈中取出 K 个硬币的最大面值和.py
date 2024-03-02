class Solution:
    def maxValueOfCoins(self, p: List[List[int]], k: int) -> int:
        # 动态规划问题
        # 多重背包模板题
        # 就是对于每一个桶，需要分配几个空间，使得最后的结果最大
        # f[i][j]表示前i个桶分配j个空间的最大值是多少
        # 选或者不选，不选就是前i-1，选就是第i个桶分配几个的问题
        # f[i][j] = max(f[i - 1][j], f[i - 1][j - 1] + sum(piles[i][:1]), f[i - 1][j - 2] + sum(piles[i][:2], f[i-1][j-j] + sum(piles[:j]))
        # f[i][j - 1] = max(f[i - 1][j - 1], f[i - 1][j - 2] + sum(piles[i][:1]))
        # 状态个数 2000 * 1000 = 2e6
        # 预处理前缀和
        f = [0] * (k + 1)
        for a in p:
            g = f[:]
            s = 0
            for i in range(len(a)):
                s += a[i]
                for j in range(i + 1, k + 1):
                    g[j] = max(g[j], f[j - (i + 1)] + s)
            f = g
        return f[-1]