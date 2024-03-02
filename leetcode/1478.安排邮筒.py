"""
f[i][j]表示前i个房间，安排j个邮箱的最短距离
那么可以枚举第j个邮箱负责的区间
f[i][j] = min(f[i0][j-1] + cost(i0 + 1, i))
"""

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()
        # 预处理出来所有房间之间如果仅仅安排一个邮箱的距离
        # f[i][j] = f[i + 1][j - 1] + houses[j] - houses[i]
        medsum = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                medsum[i][j] = medsum[i + 1][j - 1] + houses[j] - houses[i]
        # 枚举邮箱的位置
        f = [[inf] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(k, i) + 1):
                for t in range(i):
                    f[i][j] = min(f[i][j], f[t][j - 1] + medsum[t][i - 1])
        return f[n][k]