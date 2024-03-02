class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n
        self.count = n
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
        self.count -= 1
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        primes = set()
        f = defaultdict(list)
        for x in nums:
            if x == 1 and n > 1: return False
            up = x
            i = 2
            while i <= up // i:
                if up % i == 0:
                    while up % i == 0:
                        up //= i
                    primes.add(i)
                    f[x].append(i)
                i += 1
            if up > 1:
                primes.add(up)
                f[x].append(up)
        primes = list(primes)
        idx = {x: i for i, x in enumerate(primes)}
        uf = DSU(len(primes))
        for k, arr in f.items():
            for x, y in pairwise(arr):
                uf.union(idx[x], idx[y])
        return uf.count == 1