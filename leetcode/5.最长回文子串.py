class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = s[0]
        mx = 1
        f = [[True] * n for _ in range(n)]
        # f[i][j] = f[i+1][j-1] & (s[i] == s[j])
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                f[i][j] = f[i+1][j-1] and (s[i] == s[j])
                if f[i][j]:
                    if j - i + 1 > mx:
                        mx = j - i + 1
                        ans = s[i: j+1]
        return ans