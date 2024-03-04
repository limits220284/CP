class Solution:
    def cuttingRope(self, n: int) -> int:
        MOD = 10**9 + 7
        if n <= 3:return n-1
        d, m = divmod(n, 3)
        if m == 2:
            return pow(3, d, MOD) * 2 % MOD
        elif m == 1:
            return pow(3, d-1, MOD) * 4 % MOD
        return pow(3, d, MOD)
