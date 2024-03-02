class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        m, n = len(grid), len(grid[0])
        tot = m * n
        f = []
        for row in grid:
            f += row
        pre = [1] * (tot + 1)
        for i in range(tot):
            pre[i] = pre[i-1] * f[i] % mod
        suf = [1] * (tot + 1)
        for i in range(tot-1, -1, -1):
            suf[i] = suf[i+1] * f[i] % mod
        ans = [1] * tot
        for i in range(tot):
            ans[i] = pre[i-1] * suf[i+1] % mod
        res = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = ans[i * n + j]
        return res