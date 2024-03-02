class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append((y, 1))
            g[y].append((x, -1))
        ans = [0] * n
        def dfs(x, fa):
            for y, dir in g[x]:
                if y != fa:
                    ans[0] += dir < 0
                    dfs(y, x)
        dfs(0, -1)
        
        def reroot(x, fa):
            for y, dir in g[x]:
                if y != fa:
                    ans[y] = ans[x] + dir
                    reroot(y, x)
        reroot(0, -1)
        return ans