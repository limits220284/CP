class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        MX = 10 ** 9 + 7
        m, n = len(heights), len(heights[0])
        g = [[] for _ in range(m * n)]
        for i in range(m):
            for j in range(n):
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n:
                        g[i * n + j].append((abs(heights[x][y] - heights[i][j]), x * n + y))
        dis = [MX] * (m * n)
        dis[0] = 0
        vis = [False] * (m * n)
        h = [(0, 0)]
        while h:
            d, x = heappop(h)
            if vis[x]: continue
            vis[x] = True
            if x == m * n - 1:
                break
            for t, y in g[x]:
                if max(t, d) < dis[y]:
                    dis[y] = max(t, d)
                    heappush(h, (dis[y], y))
        return dis[m * n - 1]
    # 并查集的解法, 对于最小值进行排序，然后依次加入，看看能否联通，或者是二分这个答案，然后从起点开始bfs，看能否到达最后一个点
    # def minimumEffortPath(self, heights: List[List[int]]) -> int:
        