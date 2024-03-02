class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        # f[i][0] = max(f[i-1][0], f[i-1][1] + prices[i])
        # f[i][1] = max(f[i-1][1], f[i-2][0] - prices[i])
        # f[i+2][0] = max(f[i+1][0], f[i+1][1] + prices[i-2])
        # f[i+2][1] = max(f[i+1][1], f[i][0] - prices[i-2])
        n = len(prices)
        f = [[-inf, -inf] for _ in range(n+2)]
        f[1][0] = f[0][0] = 0
        # f[0][0] = f[0][1] = 0
        for i in range(n):
            f[i+2][0] = max(f[i+1][0], f[i+1][1] + prices[i-2])
            f[i+2][1] = max(f[i+1][1], f[i][0] - prices[i-2])
        return f[n+1][0]
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, hold):
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1, True), dfs(i-2, False) - prices[i])
            return max(dfs(i-1, False), dfs(i-1, True) + prices[i])
        return dfs(n-1, False)