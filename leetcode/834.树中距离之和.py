class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        ans = [0] * n
        size = [0] * n
        def dfs(x, fa, depth):
            ans[0] += depth
            res = 0
            for y in g[x]:
                if y != fa:
                    res += dfs(y, x, depth + 1)
            size[x] = res + 1
            return res + 1
        dfs(0, -1, 0)
        def reroot(x, fa):
            for y in g[x]:
                if y != fa:
                    ans[y] = ans[x] + n - 2 * size[y]
                    reroot(y, x)
        reroot(0, -1)
        return ans