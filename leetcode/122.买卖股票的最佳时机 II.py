class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        # 抽象成找多个序数对,使得多个序数对的差值最大,而且不能重合
        n = len(prices)
        ans = 0
        for i in range(n-1):
            if prices[i+1] > prices[i]:
                ans += prices[i+1] - prices[i]
        return ans
    # 动态规划，从记忆化搜索到递推
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, hold):
            if i < 0:
                return 0 if not hold else -inf
            if hold:
                return max(dfs(i-1, True), dfs(i-1, False) - prices[i])
            return max(dfs(i-1, False), dfs(i-1, True) + prices[i])
        return dfs(n-1, False)
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [[-inf, -inf] for _ in range(n+1)]
        f[0][0] = 0
        for i in range(1, n+1):
            f[i][0] = max(f[i-1][0], f[i-1][1] + prices[i-1])
            f[i][1] = max(f[i-1][1], f[i-1][0] - prices[i-1])
        return f[n][0]