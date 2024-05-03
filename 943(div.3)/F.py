import sys
input = lambda: sys.stdin.readline().strip()
from collections import defaultdict
from bisect import *


def solve():
    n, q = map(int, input().split())
    a = [int(i) for i in input().split()]

    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] ^ a[i]
    lookup = defaultdict(list)
    for i, x in enumerate(pre):
        lookup[x].append(i)

    for _ in range(q):
        l, r = map(int, input().split())
        left = lookup[pre[r]][bisect_left(lookup[pre[r]], l)] # 1
        right = lookup[pre[l - 1]][bisect_left(lookup[pre[l - 1]], r + 1) - 1] #
        print("YES" if left <= right else "NO")
    print()

T = int(input())
for _ in range(T):
    solve()