"""
每次将小于q的边加入集合中，然后看一下左上角联通的大小
"""
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return
        if x < y:
            x, y = y, x
        self.size[x] += self.size[y]
        self.p[y] = x
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        k = len(queries)
        edges = []
        for i in range(1, m):
            x, y = (i - 1) * n, i * n
            edges.append((x, y, max(grid[i - 1][0], grid[i][0])))
        for j in range(1, n):
            x, y = j - 1, j
            edges.append((x, y, max(grid[0][j - 1], grid[0][j])))
        for i in range(1, m):
            for j in range(1, n):
                x, y = i * n + j - 1, i * n + j
                edges.append((x, y, max(grid[i][j - 1], grid[i][j])))
                x, y = (i - 1) * n + j, i * n + j
                edges.append((x, y, max(grid[i - 1][j], grid[i][j])))
        edges.sort(key = lambda x: x[2])
        ln = len(edges)
        uf = DSU(m * n)
        queries_idx = list(zip(queries, range(k)))
        queries_idx.sort()
        ans = [0] * k
        i = 0
        for query, idx in queries_idx:
            while i < ln and edges[i][2] < query:
                x, y, _ = edges[i]
                uf.union(x, y)
                i += 1
            if grid[0][0] < query:
                ans[idx] = uf.size[uf.find(0)]
        return ans