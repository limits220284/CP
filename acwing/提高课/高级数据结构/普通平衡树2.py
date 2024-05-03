# 树状数组 + 二分的写法
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tr = [0] * (n + 1)

    def lowbit(self, x):
        return x & -x

    def add(self, x, c):
        i = x
        while i <= self.n:
            self.tr[i] += c
            i += self.lowbit(i)

    def sum(self, x):
        res = 0
        i = x
        while i > 0:
            res += self.tr[i]
            i -= self.lowbit(i)
        return res

    def query(self, l, r):
        return self.sum(r) - self.sum(l - 1)


# 离散化 + 树状数组
n = int(input())
N = 10 ** 7  # 最大的数不超过10^7
bit = FenwickTree(2 * N + 1)
for i in range(n):
    opt, x = map(int, input().split())
    if opt == 1:
        bit.add(x + N + 1, 1)  # 最小的数映射到1中
    elif opt == 2:
        bit.add(x + N + 1, -1)
    elif opt == 3:
        print(bit.query(1, x + N) + 1)
    elif opt == 4:
        l, r = 1, len(bit.tr)
        while l < r:
            mid = (l + r) // 2
            if bit.query(1, mid) >= x:
                r = mid
            else:
                l = mid + 1
        print(l - N - 1)
    elif opt == 5:
        diff = bit.query(x + N + 1, x + N + 1)
        if diff == 0:
            target = bit.query(1, x + N)
            l, r = 1, len(bit.tr)
            while l < r:
                mid = (l + r) // 2
                if bit.query(1, mid) >= target:
                    r = mid
                else:
                    l = mid + 1
            print(l - N - 1)
        else:
            target = bit.query(1, x + N)
            l, r = 1, len(bit.tr)
            while l < r:
                mid = (l + r) // 2
                if bit.query(1, mid) >= target:
                    r = mid
                else:
                    l = mid + 1
            print(l - N - 1)

    else:
        target = bit.query(1, x + N + 1)
        l, r = 1, len(bit.tr)
        while l < r:
            mid = (l + r) // 2
            if bit.query(1, mid) >= target + 1:
                r = mid
            else:
                l = mid + 1
        print(l - N - 1)

