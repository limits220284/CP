class Solution:
    def mincostTickets1(self, day: List[int], cost: List[int]) -> int:
        # f[i]表示days[i]的最小花费
        # dfs(i, j) i表示能够旅游到days[i]天的最小花费, j表示剩余的天数
        # dfs(i, j) = min(dfs(i+1, j), dfs(i+1, j + 1) + cost[0], ...)
        n = len(day)
        day = set(day)
        @cache
        def dfs(d):
            if d <= 0: return 0
            if d not in day:
                return dfs(d - 1)
            return min(dfs(d-1) + cost[0], dfs(d-7) + cost[1], dfs(d-30) + cost[2])
        return dfs(max(day))
    def mincostTickets(self, day: List[int], cost: List[int]) -> int:
        # 动态规划解法
        n = len(day)
        day = set(day)
        mx = max(day)
        f = [0] * (mx + 31)
        for i in range(mx + 1):
            if i not in day:
                f[i + 30] = f[i + 29]
            else:
                f[i + 30] = min(f[i + 29] + cost[0], f[i + 23] + cost[1], f[i] + cost[2])
        return f[-1]