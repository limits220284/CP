class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        g = [[] * n for _ in  range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        # print(g)
        def dfs(x):
            res = 1 # 本身自己这个点
            vis[x] = True
            for y in g[x]:
                if vis[y]: continue
                res += dfs(y)
            return res
        vis = [False] * n
        ans = []
        for i in range(n):
            if not vis[i]:
                ans.append(dfs(i))
                # print(i, vis)
        # print(ans)
        res = 0
        s = 0
        for i, x in enumerate(ans):
            res += x * s
            s += x
        return res

        