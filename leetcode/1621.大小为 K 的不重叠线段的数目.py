# 组合数学或者线性dp
# f[i][j] 表示前i个点，覆盖j个不同的线段的方案数, 考虑第j个线段覆盖多少个点
# 因为至少覆盖两个点，那么可以枚举, 或者不进行覆盖
# 1、选择覆盖第i个点：f[i][j] = f[i - 1][j - 1] + f[i - 2][j - 1] + f[i - 3][j - 1] + ...
# 2、选择不覆盖第i个点: f[i][j] = f[i - 1][j] 
# f[i][j] = f[i - 1][j] + f[i - 1][j - 1] + f[i - 2][j - 1] + f[i - 3][j - 1] + ...
# f[i - 1][j] - f[i - 2][j] = f[i - 2][j - 1] + f[i - 2][j - 1] + f[i - 3][j - 1] + ...
# 改：f[i][j] = f[i - 1][j] + f[i - 1][j - 1] + f[i - 1][j] - f[i - 2][j]
# f[i][j] = f[i - 1][j] 
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        f = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            f[i][0] = 1
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                f[i][j] = f[i - 1][j] + f[i - 1][j - 1] + f[i - 1][j] - f[i - 2][j] % MOD
        return f[-1][-1] % MOD
        