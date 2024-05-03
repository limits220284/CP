import math
import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    x = list(map(int, input().split()))
    ans = []
    ans.append(x[0] + 1)
    for i in range(1, n - 1):
        k = math.ceil((x[i] + 1 - x[i-1]) / ans[-1])
        ans.append(ans[-1] * k + x[i - 1])
    ans.append(x[-1])
    for a in ans:
        print(a, end = " ")
    print()
T = int(input())
for _ in range(T):
    solve()