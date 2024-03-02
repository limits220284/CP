MOD = 1_000_000_007
MX = 100_000

# 组合数模板
fac = [0] * MX
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD

inv_fac = [0] * MX
inv_fac[MX - 1] = pow(fac[MX - 1], MOD - 2, MOD)
for i in range(MX - 1, 0, -1):
    inv_fac[i - 1] = inv_fac[i] * i % MOD

def comb(n: int, k: int) -> int:
    return fac[n] * inv_fac[k] % MOD * inv_fac[n - k] % MOD

class Solution:
    def numberOfSequence(self, n: int, a: List[int]) -> int:
        m = len(a)
        total = n - m
        ans = comb(total, a[0]) * comb(total - a[0], n - a[-1] - 1) % MOD
        total -= a[0] + n - a[-1] - 1
        e = 0
        for p, q in pairwise(a):
            k = q - p - 1
            if k:
                e += k - 1
                ans = ans * comb(total, k) % MOD
                total -= k
        return ans * pow(2, e, MOD) % MOD