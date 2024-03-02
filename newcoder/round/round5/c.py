x = input().split()
n, l, r = int(x[0]), int(x[1]), int(x[2])
s = input()
dic = {}
for _ in range(n-1):
    x = input().split()
    u, v = int(x[0]), int(x[1])
    if u not in dic:
        dic[u] = [v]
    else:
        dic[u].append(v)
    if v not in dic:
        dic[v] = [u]
    else:
        dic[v].append(u)
vis = [0] * (n + 1)
def dfs(v, tot, l, r, f):
    tot = tot * 2 + int(s[v - 1])
    if tot > r:
        return 0
    vis[v] = 1
    if tot >= l:
        nums = f
        for u in dic[v]:
            if vis[u] == 0:
                nums += dfs(u, tot, l, r, 1)
        vis[v] = 0
        return nums
    else:
        nums = 0
        for u in dic[v]:
            if vis[u] == 0:
                nums += dfs(u, tot, l, r, 1)
        vis[v] = 0
        return nums
ans = 0
for i in range(1, n + 1):
    ans += dfs(i, 0, l, r, 0)
print(ans)