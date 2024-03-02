class Solution:
    def coinChange(self, w: List[int], amount: int) -> int:
        # 完全背包问题
        # f[i][j] 表示前i个硬币搞出j大小的所需的最小的个数
        # f[i][j] = min(f[i-1][j], f[i-1][j-w[i]]+1, f[i-1][j-2w[i]]+2, ...)
        # f[i][j-w[i]] = min(f[i-1][j-w[i]], f[i-1][j-2w[i]]+1, ...)
        # f[i][j] = min(f[i-1][j], f[i][j-w[i]] + 1)
        n = len(w)
        f = [[inf] * (amount + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(amount + 1):
                f[i][j] = f[i-1][j]
                if j >= w[i-1]:
                    f[i][j] = min(f[i - 1][j], f[i][j - w[i-1]] + 1)
        return -1 if f[-1][-1] == inf else f[-1][-1]