MOD = 10 ** 9 + 7
@cache
def dfs(i, l, e, t):
    if i == 0:
        return 1 if l == e == t == 0 else 0
    res = 0
    # 选l
    res += dfs(i - 1, 0, e, t)
    # 选 e
    res += dfs(i - 1, l, max(e - 1, 0), t)
    # 选t
    res += dfs(i - 1, l, e, 0)
    # 选其他数字
    res += dfs(i - 1, l, e, t) * 23
    return res % MOD
class Solution:
    def stringCount(self, n: int) -> int:
        return dfs(n, 1, 2, 1)
        # MOD= 10 ** 9 + 7
        # ans = pow(26, n, MOD)
        # ans -= pow(25, n - 1, MOD) * (75 + n)
        # ans += pow(24, n - 1, MOD) * (72 + 2 * n)
        # ans -= pow(23, n - 1, MOD) * (23 + n)
        # return ans % MOD