class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        ans = 0
        n = len(roads) + 1
        g = [[] for _ in range(n)]
        for x, y in roads:
            g[x].append(y)
            g[y].append(x)
        g[0].append(-1)
        def dfs(x, fa):
            nonlocal ans
            if len(g[x]) == 1:
                return 1
            res= 0
            for y in g[x]:
                if y != fa:
                    t = dfs(y, x)
                    res += t
                    ans += math.ceil(t / seats)
            return res + 1
        dfs(0, -1)
        return ans