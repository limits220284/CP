class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        def qmi(a, k):
            res = 1
            while k:
                if k & 1:
                    res = res * a
                k >>= 1
                a = a ** 2
            return res
        def max(a, b):
            return a if a > b else b
            
        @cache
        def dfs(x, fa, cnt):
            if cnt >= 16:
                return 0
            res1 = (coins[x] >> cnt) - k
            res2 = coins[x] >> (cnt + 1)
            for y in g[x]:
                if y != fa:
                    res1 += dfs(y, x, cnt)
                    res2 += dfs(y, x, cnt + 1)
            return max(res1, res2)
        return dfs(0, -1, 0)