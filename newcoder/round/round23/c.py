import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
for i in range(1, n + 1):
    if i % 2 == 1:
        print(i, end=" ")
