class Solution:
    def maxPower(self, s: str) -> int:
        i, n = 0, len(s)
        ans = 0
        while i < n:
            start = i
            while i < n-1 and s[i] == s[i+1]:
                i += 1
            ans = max(ans, i - start + 1)
            i += 1
        return ans