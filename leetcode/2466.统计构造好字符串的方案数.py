class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # f[i] 表示构造长度为i的方案数
        # f[i] = f[i-1] + zero if zero == 1, one if one == 1
        f = [0] * (high + 1)
        f[0] = 1
        ans = 0
        for i in range(1, high + 1):
            if i >= zero:
                f[i] = f[i] + f[i - zero]
            if i >= one:
                f[i] = f[i] + f[i - one]
            if i >= low:
                ans = (ans + f[i]) % (10 ** 9 + 7)
        return ans