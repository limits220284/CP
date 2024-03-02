class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        g = [[inf] * n for _ in range(n)]
        for x, y, w in roads:
            g[x][y] = g[y][x] = min(g[x][y], g[y][x], w)
        def check(f, mask):
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        f[i][j] = min(f[i][j], f[i][k] + f[k][j])
            points = []
            for i in range(n):
                if (mask >> i) & 1 == 0:
                    points.append(i)
            for x in points:
                for y in points:
                    if x == y: continue
                    if f[x][y] > maxDistance:
                        return False
            return True
        ans = 0
        for mask in range(1 << n):
            f = deepcopy(g)
            for j in range(n):
                if (mask >> j) & 1:
                    for k in range(n):
                        f[j][k] = inf
                        f[k][j] = inf
            if check(f, mask):
                ans += 1
        return ans