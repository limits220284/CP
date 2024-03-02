class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        f = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append([i, j])
                else:
                    f[i][j] = grid[i][j]
        step = 0
        while q:
            tot = len(q)
            for _ in range(tot):
                x, y = q.popleft()
                f[x][y] = str(step)
                for dx, dy in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                    if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 0:
                        q.append([dx, dy])
                        grid[dx][dy] = 1
            step += 1
        def check(mid):
            q = deque([(0, 0)])
            step = mid
            vis = {}
            while q:
                tot = len(q)
                step += 1
                for _ in range(tot):
                    x, y = q.popleft()
                    if x == m - 1 and y == n - 1:
                        return True
                    for dx, dy in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                        if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in vis:
                            if f[dx][dy] == 0:
                                q.append((dx, dy))
                                vis[(dx, dy)] = True
                            elif f[dx][dy] != 2:
                                c = int(f[dx][dy])
                                if c > step or (dx == m - 1 and dy == n - 1 and c >= step):
                                    q.append((dx, dy))
                                    vis[(dx, dy)] = True
            return False
        l, r = 0, 10 ** 9
        while l < r:
            mid = (l + r) // 2
            if check(mid) == False:
                r = mid
            else:
                l = mid + 1
        if check(l) == False:
            return l - 1
        return 10 ** 9