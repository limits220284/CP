class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        # 建图,跑两次dfs
        n = len(edges)
        g = [[] for _ in range(n+1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        cnt0 = 0
        s = {(x,y) for x,y in guesses}
        def dfs(x, fa):
            nonlocal cnt0
            for y in g[x]:
                if y != fa:
                    if (x, y) in s:
                        cnt0 += 1
                    dfs(y, x)
            return cnt0
        dfs(0, -1)
        ans = 0
        def reroot(x, fa, cnt):
            nonlocal ans
            if cnt >= k:
                ans += 1
            for y in g[x]:
                if y != fa:
                    reroot(y, x, cnt - ((x, y) in s) + ((y, x) in s))
        reroot(0, -1, cnt0)
        return ans
            
            