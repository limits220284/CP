import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

T = int(input())

def solve():
    n, m = map(int, input().split())
    a = input()
    b = input()
    def check(mid):
        i, j = 0, 0
        while i < mid and j < m:
            if a[i] == b[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == mid
    l, r = 0, n
    while l < r:
        mid = (l + r + 1) // 2
        if check(mid):
            l = mid
        else:
            r = mid - 1
    print(l)
for _ in range(T):
    solve()