class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i: int, j: int, hold: bool) -> int:
            if j < 0:
                return -inf
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, j, True), dfs(i - 1, j - 1, False) - prices[i])
            return max(dfs(i - 1, j, False), dfs(i - 1, j, True) + prices[i])
        return dfs(n - 1, k, False)
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # f[i][k][0] = max(f[i-1][k][0], f[i-1][k-1][1] + prices[i])
        # f[i][k][1] = max(f[i-1][k][1], f[i-1][k-1][0] - prices[i])
        # f[i+1][j+1][0] = max(f[i][j+1][0], f[i][j][1] + prices[i])
        # f[i+1][j+1][1] = max(f[i][j+1][1], f[i][j+1][0] - prices[i])
        f = [[[-inf, -inf] for _ in range(k+2)] for _ in range(n+1)]
        for i in range(1, k+2): f[0][i][0] = 0
        for i in range(n):
            for j in range(k+1):
                f[i+1][j+1][0] = max(f[i][j+1][0], f[i][j+1][1] + prices[i])
                f[i+1][j+1][1] = max(f[i][j+1][1], f[i][j][0] - prices[i])
        return f[n][k+1][0]
    