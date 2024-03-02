class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        # 动态规划
        # f[i][j]表示以a[i], b[j]结尾的最长公共子序列
        # f[i][j] = max(f[i-1][j-1], f[i-1][j], f[i][j-1], f[i][j])
        m, n = len(a), len(b)
        f = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                f[i][j] = max(f[i-1][j], f[i][j-1])
                if a[i-1] == b[j-1]: f[i][j] = max(f[i][j], f[i-1][j-1] + 1)
        return f[m][n]