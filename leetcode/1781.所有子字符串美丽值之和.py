class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            cnt = Counter()
            mx = 0
            for j in range(i, len(s)):
                cnt[s[j]] += 1
                mx = max(mx, cnt[s[j]])
                res += mx - min(cnt.values())
        return res