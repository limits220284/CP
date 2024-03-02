class Solution:
    def numTilings(self, n: int) -> int:
        # 无须找规律，这种题目，直接嗯算
        # 状态压缩dp
        MOD = 10 ** 9 + 7
        f = [[0] * 4 for _ in range(n+1)]
        f[0][3] = 1
        for i in range(1, n + 1):
            f[i][0] = f[i-1][3]
            f[i][1] = f[i-1][0] + f[i-1][2]
            f[i][2] = f[i-1][0] + f[i-1][1]
            f[i][3] = f[i-1][0] + f[i-1][1] + f[i-1][2] + f[i-1][3]
        return f[n][3] % MOD