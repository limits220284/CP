# 预处理筛选质数, 埃氏筛法
MX = 10 ** 5 + 1
isPrime = [True] * MX
isPrime[1] = False
for i in range(2, MX):
    if isPrime[i]:
        for j in range(i ** 2, MX, i):
            isPrime[j] = False
class DSU:
    def __init__(self, n):
        self.size = [1] * (n+1)
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.size[y] += self.size[x]
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.size[x] += self.size[y]
        else:
            self.parent[x] = y
            self.rank[y] += 1
            self.size[y] += self.size[x]
class Solution:
    def countPaths1(self, n: int, edges: List[List[int]]) -> int:
        # 枚举所有的质数，然后统计以这个数为根能够形成多少非质数的连通块，比如 a, b, c
        # 那么最后的结果就是a *  b, a * c, b * c
        # 并查集的解法
        g = [[] for _ in range(n + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        def dfs(x, fa):
            nodes.append(x)
            for y in g[x]:
                if y != fa:
                    if not isPrime[y]:
                        dfs(y, x)
        ans = 0
        size = [0] * (n + 1)
        for x in range(1, n+1):
            if not isPrime[x]:
                continue
            s = 0
            for y in g[x]:
                if isPrime[y]:
                    continue
                if size[y] == 0:
                    nodes = []
                    dfs(y, -1)
                    for z in nodes:
                        size[z] = len(nodes)
                ans += size[y] * s
                s += size[y]
            ans += s
        return ans
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        # 并查集解法, 将所有的非质数节点联通到一起
        g = [[] for _ in range(n + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        uf = DSU(n+1)
        for x, y in edges:
            if not isPrime[x] and not isPrime[y]:
                uf.union(x, y)
        ans = 0
        for x in range(1, n + 1):
            if not isPrime[x]:
                continue
            st = set()
            for y in g[x]:
                if isPrime[y]:
                    continue
                p = uf.find(y)
                if p not in st:
                    st.add(p)
            st = [uf.size[x] for x in st]
            ans += sum(st)
            # 这个地方超时了, 用前缀和进行优化                                                                                                                          
            s = 0
            for i in range(len(st)):
                ans += s * st[i]
                s += st[i]
        return ans