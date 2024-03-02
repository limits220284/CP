class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n
        self.cnt = n
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.size[x] += self.size[y]
        self.p[y] = x
        self.cnt -= 1
class Solution:
    def regionsBySlashes(self, f: List[str]) -> int:
        m = len(f)
        n = len(f[0])
        uf = DSU(2 * m * n)
        for i in range(m):
            for j in range(n):
                a, b = 2 * (i * n + j), 2 * (i * n + j) + 1
                if f[i][j] == ' ':
                    uf.union(a, b) # 将自己和自己连接起来
                if i - 1 >= 0:
                    x, y = 2 * ((i - 1) * n + j), 2 * ((i - 1) * n + j) + 1
                    if f[i][j] == '\\':
                        if f[i - 1][j] == ' ' or f[i - 1][j] == '\\':
                            uf.union(b, x)
                        else:
                            uf.union(b, y)
                    elif f[i][j] == '/':
                        if f[i - 1][j] == ' ' or f[i - 1][j] == '/':
                            uf.union(a, y)
                        else:
                            uf.union(a, x)
                    else:
                        if f[i - 1][j] == ' ' or f[i - 1][j] == '/':
                            uf.union(a, y)
                        else:
                            uf.union(a, x)
                if j - 1 >= 0:
                    x, y = 2 * (i * n + j - 1), 2 * (i * n + j - 1) + 1
                    uf.union(a, y)
        return uf.cnt