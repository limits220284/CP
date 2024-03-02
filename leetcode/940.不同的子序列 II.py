MOD = 10 ** 9 + 7

class Solution:
    # 记录最后一个位置的版本
    def distinctSubseqII1(self, s: str) -> int:
        n = len(s)
        f = [[0] * 26 for _ in range(n)]
        for i, c in enumerate(s):
            x = ord(c) - ord('a')
            f[i] = f[i-1][::]
            f[i][x] = (sum(f[i-1]) + 1) % MOD
        return sum(f[-1]) % MOD
    # 空间优化版本
    def distinctSubseqII2(self, s: str) -> int:
        n = len(s)
        f = [0] * 26
        for i, c in enumerate(s):
            x = ord(c) - ord('a')
            f[x] = (sum(f) + 1) % MOD
        return sum(f) % MOD
    # 再次优化
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        f = [0] * 26
        curans = 1
        for c in s:
            x = ord(c) - ord('a')
            newcount = curans
            curans = (curans + newcount - f[x]) % MOD
            f[x] = newcount
        return (curans - 1) % MOD