class Solution:
    def makeFancyString(self, s: str) -> str:
        i, n = 0, len(s)
        ans = ""
        while i < n:
            start = i
            while i < n-1 and s[i] == s[i+1]:
                i += 1
            if i - start + 1 < 3:
                ans += s[start:i+1]
            else:
                ans += s[start: start + 2]
            i += 1
        return ans