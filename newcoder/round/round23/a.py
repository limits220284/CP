import sys
from sortedcontainers import SortedList
input = lambda: sys.stdin.readline().strip()

st = SortedList()

def solve():
    x, y = map(int, input().split())
    if x >= y:
        print(-1, -1)
    else:
        print(1, y - x)

t = int(input())

for _ in range(t):
    solve()

