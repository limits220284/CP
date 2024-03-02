"""
# 推公式
f[i, j] = f[i-1, j] + f[i-1, j-vi] + f[i-1, j-2vi] + f[i-1, j-3vi] + ... + f[i-1, j-aivi]
f[i, j-vi] - f[i-1, j-(ai+1)vi] = f[i-1, j-vi] + f[i-1, j-2vi] + f[i-1, j-3vi] + f[i-1, j-4vi] + ... + f[i-1, j-aivi]
f[i, j] = f[i-1, j] + f[i, j-vi] - f[i-1, j-(ai+1)vi]
"""
class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        MOD = 10 ** 9 + 7
        cnt = Counter(nums)
        v = list(cnt.keys())
        n = len(cnt)
        f = [[0] * (r + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i in range(1, n + 1):
            t = cnt[v[i-1]]
            for j in range(r + 1):
                f[i][j] = f[i - 1][j]
                if j >= v[i - 1]:
                    f[i][j] += f[i][j - v[i - 1]]
                if j >= (t + 1) * v[i-1]:
                    f[i][j] -= f[i-1][j - (t + 1) * v[i-1]]
        ans = 0
        for i in range(l, r + 1):
            ans = (ans + f[-1][i]) % MOD
        return ans * (1 + cnt[0]) % MOD