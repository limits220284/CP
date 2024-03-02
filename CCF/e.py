import sys
from collections import *

input = lambda: sys.stdin.readline().rstrip("\r\n")

N = int(input())
pri = []
not_prime = [False] * (N + 1)
d = [0] * (N + 1)
num = [0] * (N + 1)


def pre(n):
    d[1] = 1
    for i in range(2, n + 1):
        if not not_prime[i]:
            pri.append(i)
            d[i] = 2
            num[i] = 1
        for pri_j in pri:
            if i * pri_j > n:
                break
            not_prime[i * pri_j] = True
            if i % pri_j == 0:
                num[i * pri_j] = num[i] + 1
                d[i * pri_j] = d[i] // num[i * pri_j] * (num[i * pri_j] + 1)
                break
            num[i * pri_j] = 1
            d[i * pri_j] = d[i] * 2


pre(N)
# print(d)
hsh = Counter(pri)
ans = 0
for x in pri:
    rest = N - x
    if rest == 0:
        continue
    if rest in hsh:
        continue
    ans += d[rest]
print(ans)
