class DSU:
    def __init__(self, n):
        self.p = list(range(n + 1))
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a == b: return
        self.p[a] = b
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # 贪心的想一想，先加入type三的肯定是最好的
        edges.sort(key = lambda x: x[0], reverse = True)
        ufa = DSU(n)
        ufb = DSU(n)
        ans = 0
        for t, u, v in edges:
            if t == 1:
                a, b = ufa.find(u), ufa.find(v)
                if a == b:
                    ans += 1
                else:
                    ufa.union(u, v)
            elif t == 2:
                a, b = ufb.find(u), ufb.find(v)
                if a == b:
                    ans += 1
                else:
                    ufb.union(u, v)
            elif t == 3:
                a, b = ufa.find(u), ufa.find(v)
                c, d = ufb.find(u), ufb.find(v)
                if a == b and c == d:
                    ans += 1
                else:
                    ufa.union(u, v)
                    ufb.union(u, v)
        # 计算ufa, ufb的联通数量
        for x, y in pairwise(range(1, n + 1)):
            a, b = ufa.find(x), ufa.find(y)
            c, d = ufb.find(x), ufb.find(y)
            if a != b or c != d:
                return -1
        return ans