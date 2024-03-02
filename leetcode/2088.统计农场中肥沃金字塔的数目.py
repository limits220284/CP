class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        # dp[i][j]表示(i, j)形成金字塔的层数
        # g[i][j] = min(g[i-1][j], g[i-1][j-1], g[i-1][j+1]) + 1
        m, n = len(grid), len(grid[0])
        def dfs(g):
            res = 0
            for i in range(m - 2, -1, -1):
                for j in range(1, n - 1):
                    if grid[i][j] == 0: continue
                    g[i][j] = min(g[i + 1][j], g[i + 1][j-1], g[i + 1][j+1]) + 1
                    res += g[i][j] - 1
            print(g)
            return res
        ans = 0
        ans += dfs(deepcopy(grid))
        # # 将矩阵反转
        print("ok", grid)
        for i in range(m // 2):
            grid[i], grid[m - 1 - i] = grid[m - 1 - i], grid[i]
        print(grid)
        ans += dfs(deepcopy(grid))
        return ans
