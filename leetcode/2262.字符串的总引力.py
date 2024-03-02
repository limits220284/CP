class Solution:
    def appealSum(self, s: str) -> int:
        lasts = [-1] * 26
        ans = 0
        n = len(s)
        for i, c in enumerate(s):
            ans += (i - lasts[ord(s[i]) - ord('a')]) * (n - i)
            lasts[ord(s[i]) - ord('a')] = i
        return ans
            