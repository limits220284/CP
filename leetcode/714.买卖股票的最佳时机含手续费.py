class Solution:
    def maxProfit1(self, prices: List[int], fee: int) -> int:
        # 动态规划
        # f[i][0] = max(f[i-1][0], f[i-1][1] + prices[i])
        # f[i][1] = max(f[i-1][1], f[i-1][0] - prices[i] - fee)
        n = len(prices)
        f = [[-inf, -inf] for _ in range(n+1)]
        f[0][0] = 0
        for i in range(1, n+1):
            f[i][0] = max(f[i-1][0], f[i-1][1] + prices[i-1] - fee)
            f[i][1] = max(f[i-1][1], f[i-1][0] - prices[i-1])
        return max(f[n])
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        @cache
        def dfs(i: int, hold: bool) -> int:
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1, True), dfs(i-1, False) - prices[i] - fee)
            return max(dfs(i-1, False), dfs(i-1, True) + prices[i])
        return max(dfs(n-1, False), dfs(n-1, True))