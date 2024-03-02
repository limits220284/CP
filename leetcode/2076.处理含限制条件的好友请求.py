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
        if self.size[x] > self.size[y]:
            x, y = y, x
        self.size[x] += self.size[y]
        self.p[y] = x
    def connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = DSU(n)
        m = len(requests)
        ans = []
        for i in range(m):
            x, y = uf.find(requests[i][0]), uf.find(requests[i][1])
            if x != y:
                check = True
                for res in restrictions:
                    u, v = uf.find(res[0]), uf.find(res[1])
                    if (x == u and y == v) or (x == v and y == u):
                        check = False
                        break
                if check:
                    ans.append(True)
                    uf.union(x, y)
                else:
                    ans.append(False)
            else:
                ans.append(True)
        return ans
