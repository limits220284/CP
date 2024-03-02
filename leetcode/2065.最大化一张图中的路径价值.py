class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, w))
        ans = 0
        dic = defaultdict(int)
        tot = 0
        def dfs(x, cost):
            nonlocal tot, ans
            if cost > maxTime:
                return
            dic[x] += 1
            if dic[x] == 1:
                tot += values[x]
            if x == 0:
                ans = max(ans, tot)
            for y, w in g[x]:
                dfs(y, cost + w)
            dic[x] -= 1
            if dic[x] == 0:
                tot -= values[x]
        dfs(0, 0)
        return ans