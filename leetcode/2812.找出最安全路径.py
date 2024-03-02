class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return 0
        m, n = len(grid), len(grid[0])
        inx = [0, 0, -1, 1]
        iny = [-1, 1, 0, 0]
        q = deque()
        vis = {}
        rmx = [[0] * n for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    vis[(i, j)] = True
        dep = 1
        while q:
            tot = len(q)
            for i in range(tot):
                x, y = q.popleft()
                for k in range(4):
                    dx, dy = x + inx[k], y + iny[k]
                    if 0 <= dx < n and 0 <= dy < n and (dx, dy) not in vis:
                        vis[(dx, dy)] = True
                        q.append((dx, dy))
                        rmx[dx][dy] = dep
            dep += 1
        
        g = [[] for _ in range(2 * n)]
        for i in range(n):
            for j in range(n):
                g[rmx[i][j]].append((i, j))
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]
        p = list(range(n**2))
        for i in range(2 * n - 1, -1, -1):
            for x, y in g[i]:
                for k in range(4):
                    dx, dy = x + inx[k], y + iny[k]
                    if 0 <= dx < n and 0 <= dy < n and rmx[dx][dy] >= rmx[x][y]:
                        fa, fb = find(x * n + y), find(dx * n + dy)
                        if fa != fb:
                            p[fa] = fb
            if find(0) == find(n ** 2 - 1):
                return i
        return 0
        