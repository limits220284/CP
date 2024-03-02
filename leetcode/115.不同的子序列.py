class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # f[i][j]代表从s[:i]中出现t[:j]的个数
        # f[i][j] = f[i-1][j] + f[i-1][j-1]
        m, n = len(s), len(t)
        f = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m): f[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                f[i][j] = f[i-1][j]
                if s[i-1] == t[j-1]:
                    f[i][j] += f[i-1][j-1]
        return f[m][n]
                
