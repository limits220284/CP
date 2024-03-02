class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        vis = set()
        for x, y in connections:
            g[x].append(y)
            g[y].append(x)
            vis.add((x, y))
        def dfs(x, fa):
            t = 0
            for y in g[x]:
                if y != fa:
                    t += dfs(y, x)
                    if (x, y) in vis:
                        t += 1
            return t  
        return dfs(0, -1)