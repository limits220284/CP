class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 10 ** 9 + 7
        # k只有50，直接网格动态规划
        # 定义三维dp,能整除k，就是%k为零
        m, n = len(grid), len(grid[0])
        f = [[[0] * k for _ in range(n+1)] for _ in range(m+1)]
        f[0][0][grid[0][0] % k] += 1
        for i in range(m):
            for j in range(n):
                for t in range(k):
                    if j + 1 < n: f[i][j+1][(t + grid[i][j+1]) % k] += f[i][j][t]
                    if i + 1 < m: f[i+1][j][(t + grid[i+1][j]) % k] += f[i][j][t]

        return f[m-1][n-1][0] % mod
                
        