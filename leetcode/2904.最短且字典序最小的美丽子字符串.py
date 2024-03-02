class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # 直接暴力枚举
        if s.count('1') < k: return ""
        n = len(s)
        mx = inf
        ans = ""
        for i in range(n):
            for j in range(i, n):
                ss = s[i:j+1]
                if ss.count('1') == k:
                    m = j - i + 1
                    if m < mx:
                        mx = m
                        ans = ss
                    elif m == mx:
                        ans = min(ans, ss)
        return ans
                        