class SegmentTree:
    def __init__(self, n):
        self.f = [[0, 0, -inf] for i in range(4 * n)]
    
    def pushup(self, u):
        self.f[u][2] = max(self.f[u * 2][2], self.f[u * 2 + 1][2])
        
    def buildTree(self, u, l, r):
        self.f[u][0], self.f[u][1] = l, r
        if l >= r: 
            return 
        mid = (self.f[u][0] + self.f[u][1]) // 2
        self.buildTree(2 * u, l, mid)
        self.buildTree(2 * u + 1, mid + 1, r) 
        self.pushup(u)
    
    def update(self, u, x, v):
        if self.f[u][0] == x and self.f[u][1] == x:
            self.f[u][2] = v
            return 
        mid = (self.f[u][0] + self.f[u][1]) // 2
        if x <= mid: 
            self.update(2 * u, x, v)
        elif x > mid:
            self.update(2 * u + 1, x, v)
        self.pushup(u)
    
    def query(self, u, l, r):
        # print(u)
        if self.f[u][0] >= l and self.f[u][1] <= r:
            return self.f[u][2]
        mid = (self.f[u][0] + self.f[u][1]) // 2
        v = -inf
        if l <= mid: 
            v = self.query(2 * u, l, min(r, mid))
        if mid < r: 
            v = max(v, self.query(2 * u + 1, max(mid + 1, l), r))
        return v

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        tmp = sorted(set(x - i for i, x in enumerate(nums)))
        print(tmp)
        n = len(tmp)
        tree = SegmentTree(n + 1)
        tree.buildTree(1, 1, n)
        for i, x in enumerate(nums):
            idx = bisect_left(tmp, x - i) + 1
            print(idx)
            t = max(0, tree.query(1, 1, idx)) + x
            tree.update(1, idx, t)
        # print(tree.f)
        # print(tree.query(1, 1, n))
        return tree.query(1, 1, n)
