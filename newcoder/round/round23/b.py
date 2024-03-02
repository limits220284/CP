import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
for i in range(4 * n):
    if i < n:
        for j in range(n - i):
            print(".", end="")
        for j in range(4 * n - 2 * (n - i)):
            print("*", end="")
        for j in range(n - i):
            print(".", end="")
    elif i >= 3 * n:
        for j in range(i - 3 * n + 1):
            print(".", end="")
        for j in range(4 * n - 2 * (i - 3 * n + 1)):
            print("*", end="")
        for j in range(i - 3 * n + 1):
            print(".", end="")
    else:
        for j in range(n):
            print("*", end="")
        for j in range(4 * n - 2 * n):
            print(".", end="")
        for j in range(n):
            print("*", end="")
    print()
