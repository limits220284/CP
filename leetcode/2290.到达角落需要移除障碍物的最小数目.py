class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dis = [[inf] * n for _ in range(m)]
        dis[0][0] = 0
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < m and 0 <= dy < n:
                    g = grid[dx][dy]
                    if dis[x][y] + g < dis[dx][dy]:
                        dis[dx][dy] = dis[x][y] + g
                        if g == 0:
                            q.appendleft((dx, dy))
                        else:
                            q.append((dx, dy))
        return dis[m - 1][n - 1]
