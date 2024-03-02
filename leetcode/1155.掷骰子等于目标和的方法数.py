class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # 动态规划
        # f[i][j] 表示从前i个筛子中搞出j的方案数
        # f[i][j] += f[i-1][j-k]
        MOD = 10 ** 9 + 7
        f = [[0] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                for t in range(1, k + 1):
                    if j >= t:
                        f[i][j] = (f[i][j] + f[i-1][j-t]) % MOD
        return f[n][target] % MOD 