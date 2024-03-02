class Solution:
    def minScoreTriangulation1(self, v: List[int]) -> int:
        # f[i][j] = min(f[i][k] + f[k][j] + v[i]v[k]v[j])
        @cache
        def dfs(i, j):
            if i + 1 == j: return 0
            ans = inf
            for k in range(i + 1, j):
                ans = min(ans, dfs(i, k) + dfs(k, j) + v[i] * v[k] * v[j])
            return ans
        return dfs(0, len(v) - 1)

    def minScoreTriangulation(self, v: List[int]) -> int:
        # f[i][j] = min(f[i][k] + f[k][j] + v[i]v[k]v[j])
        # 需要知道枚举顺序
        # f[i][j]的时候需要枚举中间的k
        # 也就是说如果我想要获得f[i][j], 提前就需要计算出f[i][k]的信息, 因为k <= j，所以确定了枚举顺序为从小到大
        # 又需要知道f[k][j]，因为k > i，所以需要从大到小枚举i
        n = len(v)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                f[i][j] = inf
                for k in range(i + 1, j):
                    f[i][j] = min(f[i][j], f[i][k] + f[k][j] + v[i] * v[k] * v[j])
        return f[0][n - 1]