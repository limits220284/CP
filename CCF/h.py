import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
x = list(map(int, input().split()))
n, m, k = x[0], x[1], x[2]
G = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(k):
    x = list(map(int, input().split()))
    x1, y1, x2, y2 = x[0], x[1], x[2], x[3]
    if x1 == x2:
        y1, y2 = min(y1, y2), max(y1, y2)
        for i in range(y1, y2 + 1):
            G[x1][i] = 1
    if y1 == y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        for i in range(x1, x2 + 1):
            G[i][y1] = 1
x = list(map(int, input().split()))
px, py = x[0], x[1]
G[px][py] = 2
fx = [[0, -1], [0, 1], [1, 0], [-1, 0]]


def check(x, y):
    return x >= 1 and x <= n and y >= 1 and y <= m


h = [[px, py]]
G[px][py] = 2
wall = []
fg = False

while len(h):
    s = []
    for v in h:
        ct_1 = 0
        for f in fx:
            xx, yy = v[0] + f[0], v[1] + f[1]
            if not check(xx, yy):
                fg = True
                continue
            if G[xx][yy] == 2:
                continue
            if G[xx][yy] == 1:
                ct_1 += 1
                continue
            s.append([xx, yy])
            G[xx][yy] = 2
        if ct_1:
            wall.append(v)
    if len(s) > 0:
        h = s
        continue
    if fg:
        break
    for v in wall:
        for f in fx:
            xx, yy = v[0] + f[0], v[1] + f[1]
            if not check(xx, yy):
                fg = True
                continue
            if G[xx][yy] == 2:
                continue
            if G[xx][yy] == 1:
                s.append([xx, yy])
                G[xx][yy] = 2
    wall = []
    h = s
ct = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if G[i][j] == 0:
            ct += 1
print(ct)
