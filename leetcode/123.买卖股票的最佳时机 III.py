class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = 2
        n = len(prices)
        f = [[[-inf, -inf] for _ in range(k+2)] for _ in range(n+1)]
        for i in range(1, k+2): f[0][i][0] = 0
        for i in range(1, n+1):
            for j in range(1, k+2):
                f[i][j][0] = max(f[i-1][j][0], f[i-1][j][1] + prices[i-1])
                f[i][j][1] = max(f[i-1][j][1], f[i-1][j-1][0] - prices[i-1])
        return f[n][k+1][0]
    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, j, hold):
            if j < 0:
                return -inf
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1, j, True), dfs(i-1, j, False) - prices[i])
            return max(dfs(i-1, j, False), dfs(i-1, j-1, True) + prices[i])
        return dfs(n-1, 2, False)
    