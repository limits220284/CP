class Solution:
    def countHomogenous(self, s: str) -> int:
        # 分组循环
        MOD = 10 ** 9 + 7
        i, n = 0, len(s)
        ans = 0
        while i < n:
            start = i
            while i < n-1 and s[i] == s[i+1]:
                i += 1
            ans += (i - start + 1) * (i - start + 1 + 1) // 2
            i += 1
        return ans % MOD