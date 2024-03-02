subsets = [[] for _ in range(1 << 12)]
for i in range(1 << 12):
    s = i
    while s:
        subsets[i].append(s)
        s = (s - 1) & i
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        m = 1 << len(jobs)
        pre = [0] * m
        for i in range(1, m):
            pre[i] = pre[i^i&-i] + jobs[(i&-i).bit_length()-1]
        f = [[0] * m for _ in range(k)]
        for i in range(m): f[0][i] = pre[i]
        for i in range(1, k):
            for j in range(1, m):
                t = inf
                for s in subsets[j]:
                    v = f[i-1][j^s]
                    if pre[s] > v: v = pre[s]
                    if v < t: t = v
                f[i][j] = t
        return f[k-1][m-1]