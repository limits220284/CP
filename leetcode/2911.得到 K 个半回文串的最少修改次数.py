# 需要进行预处理出来所有的长度的公因子
# ds[i] 里面存的就是所有长度的真因子
MX = 201
ds = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i * 2, MX, i):
        ds[j].append(i)

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        def modify_cnt(ss):
            m = len(ss)
            min_cnt = inf
            # print(m, ds[m])
            for d in ds[m]:
                cnt = 0
                for i in range(d):
                    t = ss[i::d]
                    l, r = 0, len(t)-1
                    while l < r:
                        if t[l] != t[r]:
                            cnt += 1
                        l += 1
                        r -= 1
                min_cnt = min(min_cnt, cnt)
            return min_cnt
        modify = [[inf] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                modify[i][j] = modify_cnt(s[i: j + 1])
        # 划分形dp
        # f[i][j] 表示前i个字母中划分成j个子字符串，所需要的最小修改次数
        # f[i][j] = f[i-1][j-1] + cost(i-1, i), f[i-2][j-1] + cost(i-2, i) 
        f = [[inf] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for t in range(i):
                    f[i][j] = min(f[i][j], f[t][j-1] + modify[t][i-1])
        return f[n][k]