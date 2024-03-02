import sys

input = lambda: sys.stdin.readline().strip()

n, p = int(input().split())
color = input()
w = list(map(int, input().split()))


def work(arr):
    m = len(arr)
    f = [[0] * (p + 1) for _ in range(m + 1)]
    f[0][0] = 1
    for i in range(m):
        for j in range(p):
            f[i][j] = f[i - 1][j]
            if j >= p[i]:
                f[i][j] += f[i - 1][j - p[i]]
    return f[m][p]


red = []
blue = []
for i in range(n):
    if color[i] == "B":
        blue.append(w[i])
    else:
        red.append(w[i])
print(work(w) - work(red) - work(blue))
print(blue, red)
