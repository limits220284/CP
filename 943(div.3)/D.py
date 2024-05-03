import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
def solve():
    n, k, pb, ps = map(int, input().split())
    p = [0] + list(map(int, input().split()))
    a = [0] + list(map(int, input().split()))
    def work(px):
        vis = [False] * (n + 1)
        arr = []
        while vis[px] == False:
            vis[px] = True
            arr.append(a[px])
            px = p[px]
            if len(arr) >= k:
                break
        return arr
    arr1 = work(pb)
    arr2 = work(ps)
    l1, l2 = len(arr1), len(arr2)
    ans1, ans2 = arr1[0] * k, arr2[0] * k
    s = arr1[0]
    for i in range(1, l1):
        ans1 = max(ans1, s + (k - i) * arr1[i])
        s += arr1[i]
    s = arr2[0]
    for i in range(1, l2):
        ans2 = max(ans2, s + (k - i) * arr2[i])
        s += arr2[i]
    if ans1 > ans2:
        print("Bodya")
    elif ans1 < ans2:
        print("Sasha")
    else:
        print("Draw")
T = int(input())
for _ in range(T):
    solve()