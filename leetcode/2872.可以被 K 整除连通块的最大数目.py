class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        ans = 0
        def dfs(x,  fa):
            nonlocal ans
            tot = values[x]
            for y in g[x]:
                if y != fa:
                    tot += dfs(y, x)
            if tot % k == 0:
                ans += 1
            return tot
        dfs(0, -1)
        return ans