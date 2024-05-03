import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    print(1, 1)
    print(1, 2)
    for i in range(3, n + 1):
        print(i, i)

T = int(input())
for _ in range(T):
    solve()