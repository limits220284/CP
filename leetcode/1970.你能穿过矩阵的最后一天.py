class Solution:
    def latestDayToCross(self, m: int, n: int, cells: List[List[int]]) -> int:
        f = [[0] * n for _ in range(m)]
        for i, [x, y] in enumerate(cells):
            # print(x - 1, y - 1)
            f[x - 1][y - 1] = i + 1
        # print(f)
        def check(mid):
            # init
            q = deque()
            vis = set()
            for i in range(n):
                if f[0][i] > mid:
                    q.append((0, i))
                    vis.add((0, i))
            while q:
                x, y = q.popleft()
                if x == m - 1:
                    return True
                for dx, dy in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                    if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in vis and f[dx][dy] > mid:
                        vis.add((dx, dy))
                        q.append((dx, dy))
            return False
        l, r = 0, m * n
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l