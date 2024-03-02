class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        ans = [0] * n
        def dfs(x, fa):
            f, z = [], []
            if cost[x] > 0:
                z.append(cost[x])
            else:
                f.append(cost[x])
            cnt = 1
            for y in g[x]:
                if y != fa:
                    ct, zz, ff = dfs(y, x)
                    cnt += ct
                    f += ff
                    z += zz
                    if len(z) >= 3:
                        z.sort()
                        z = [z[-3], z[-2], z[-1]]
                    if len(f) >= 3:
                        f.sort()
                        f = [f[0], f[1], f[2]]
            f.sort()
            z.sort()
            if cnt < 3:
                ans[x] = 1
                return cnt, z, f
            if len(z) == 3:
                ans[x] = max(ans[x], z[-1] * z[-2] * z[-3])
                if len(f) >= 2:
                    ans[x] = max(ans[x], f[0] * f[1] * z[-1])
            elif len(z) == 2:
                if len(f) >= 2:
                    ans[x] = max(ans[x], f[0] * f[1] * z[-1])
                elif len(f) == 1:
                    ans[x] = 0
            elif len(z) == 1:
                if len(f) >= 2:
                    ans[x] = max(ans[x], f[0] * f[1] * z[-1])
            elif len(z) == 0:
                ans[x] = 0
            return cnt, z, f
        dfs(0, -1)
        return ans