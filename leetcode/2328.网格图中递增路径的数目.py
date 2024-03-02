class Solution:
    def countPaths1(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        # f[i][j]表示以i, j为结尾的递增路径的个数
        # f[i][j] += f[x][y]
        inx = [0, 0, -1, 1]
        iny = [-1, 1, 0, 0]
        @lru_cache(None)
        def f(x, y):
            res = 1
            for i in range(4):
                dx, dy = x + inx[i], y + iny[i]
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] < grid[x][y]:
                    res += f(dx, dy)
            return res
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = (ans + f(i, j)) % MOD
        return ans
    def countPaths(self, grid: List[List[int]]) -> int:
        # 拓扑排序，找入度为零的点，然后从这些点进行遍历
        # 如果找到一个递增的，就用该次数加上比他小的点的路径数
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        # f[i][j]表示以i, j为结尾的递增路径的个数
        # f[i][j] += f[x][y]
        inx = [0, 0, -1, 1]
        iny = [-1, 1, 0, 0]
        ans = [[1] * n for _ in range(m)]
        IN = [[0] * n for _ in range(m)]
        q = deque()
        for x in range(m):
            for y in range(n):
                for k in range(4):
                    dx, dy = x + inx[k], y + iny[k]
                    if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] > grid[x][y]:
                        IN[x][y] += 1
                if IN[x][y] == 0: q.append((x, y))
        while q:
            x, y = q.popleft()
            for k in range(4):
                dx, dy = x + inx[k], y + iny[k]
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] < grid[x][y]:
                    ans[dx][dy] += ans[x][y]
                    IN[dx][dy] -= 1
                    if IN[dx][dy] == 0:
                        q.append((dx, dy))
        res = 0
        for row in ans:
            for x in row:
                res = (res + x) % MOD
        return res