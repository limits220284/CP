from sortedcontainers import SortedList

class Node:
    def __init__(self, l = 0, r = 0, mx = 0):
        self.l = l
        self.r = r
        self.mx = mx
class SegmentTree:
    def __init__(self, n):
        self.f = [Node() for i in range(4 * n)]
    
    def pushup(self, u):
        self.f[u].mx = max(self.f[u * 2].mx, self.f[u * 2 + 1].mx)
    
    def pushdown(self, u):
        if self.f[u].mx:
            self.f[u * 2].mx = max(self.f[u * 2].mx, self.f[u].mx)
            self.f[u * 2 + 1].mx = max(self.f[u * 2 + 1].mx, self.f[u].mx)
            self.f[u].mx = 0
    def build(self, u, l, r):
        self.f[u].l, self.f[u].r = l, r
        if l >= r: 
            return 
        mid = (self.f[u].l + self.f[u].r) // 2
        self.build(2 * u, l, mid)
        self.build(2 * u + 1, mid + 1, r) 
        self.pushup(u)
    
    def modify(self, u, l, r, d):
        if self.f[u].l >= l and self.f[u].r <= r:
            self.f[u].mx = max(self.f[u].mx, d)
            return
        self.pushdown(u)
        mid = (self.f[u].l + self.f[u].r) // 2
        if l <= mid:
            self.modify(u * 2, l, r, d)
        if r > mid:
            self.modify(u * 2 + 1, l, r, d)
        # self.pushup(u)
    
    def query(self, u, l, r):
        if self.f[u].l >= l and self.f[u].r <= r:
            return self.f[u].mx
        self.pushdown(u)
        mid = (self.f[u].l + self.f[u].r) // 2
        v = -inf
        if l <= mid: 
            v = self.query(2 * u, l, min(r, mid))
        if mid < r: 
            v = max(v, self.query(2 * u + 1, max(mid + 1, l), r))
        return v
class Solution:
    # 线段树解法, 维护区间最大值
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 离散化排序去重
        arr = []
        for x, y, _ in buildings:
            arr.append(x)
            arr.append(y)
        arr = sorted(set(arr))
        print(arr)
        n = len(arr)
        sg = SegmentTree(n + 1)
        sg.build(1, 1, n)
        for i, [x, y, h] in enumerate(buildings):
            l, r = bisect_left(arr, x) + 1, bisect_left(arr, y)
            sg.modify(1, l, r, h) # 区间修改最大值
        maxh = -1
        ans = []
        for i in range(n):
            x = i + 1
            t = sg.query(1, x, x)
            if t != maxh:
                ans.append([arr[i], t])
                maxh = t
        return ans        

    # 平衡树解法
    def getSkyline1(self, buildings: List[List[int]]) -> List[List[int]]:
        def cmp(a, b):
            if a[0] != b[0]:
                return a[0] - b[0]
            if a[0] == b[0]:
                if a[1] != b[1]:
                    return a[1] - b[1]
                elif a[1] == 0:
                    return b[2] - a[2]
                elif a[1] == 1:
                    return a[2] - b[2]
        arr = []
        for i, [l, r, h] in enumerate(buildings):
            arr.append((l, 0, h))
            arr.append((r, 1, h))
        arr.sort(key = cmp_to_key(cmp))
        st = SortedList()
        ans = []
        maxh = -1
        for x, lr, h in arr:
            if lr == 0:
                st.add(h)        
                if st[-1] > maxh:
                    ans.append([x, h])
                    maxh = st[-1]
            else:
                st.remove(h)
                if len(st) == 0:
                    ans.append([x, 0])
                    maxh = 0
                if len(st) and maxh > st[-1]:
                    ans.append([x, st[-1]])
                    maxh = st[-1]
        return ans