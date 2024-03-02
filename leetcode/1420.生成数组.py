"""
定义f[i][j][t] 表示前i个数中最大值为j，搜索代价为t的数组的数量
由f[i - 1][~][~]转移而来
如果代价不发生变化，那么选择的第i个数就必须小于等于j
如果代价发生了变化，那么选择的第i个数就必须从前面最大值小于j的转移过来
1、f[i][j][t] += f[i-1][j][t] * (1 ~ j)
2、f[i][j][t] += f[i-1][1 ~ (j - 1)][t]

"""
class Solution:
    def numOfArrays1(self, n: int, m: int, k: int) -> int:
        if k == 0: return 0
        f = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, m + 1):
            f[1][i][1] = 1
        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for t in range(1, min(k, i) + 1):
                    f[i][j][t] += f[i - 1][j][t] * j
                    for j0 in range(1, j):
                        f[i][j][t] += f[i - 1][j0][t - 1]
        ans = sum(f[n][j][k] for j in range(1, m + 1)) % (10 ** 9 + 7)
        return ans
    
    ## 前缀和优化
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0:
            return 0
        f = [[[0] * (m + 1) for _ in range(k + 1)] for __ in range(n + 1)]
        mod = 10 ** 9 + 7
        for j in range(1, m + 1):
            f[1][1][j] = 1
        for i in range(2, n + 1):
            for s in range(1, min(k, i) + 1):
                pre = 0
                for j in range(1, m + 1):
                    f[i][s][j] = f[i - 1][s][j] * j
                    f[i][s][j] += pre
                    # for j0 in range(1, j):
                    #     f[i][s][j] += f[i - 1][s - 1][j0]
                    f[i][s][j] %= mod
                    pre += f[i - 1][s - 1][j]
        ans = sum(f[n][k][j] for j in range(1, m + 1)) % mod
        return ans