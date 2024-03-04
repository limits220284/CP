class Solution:
    def replaceSpace(self, s: str) -> str:
        ans = ''
        for c in s:
            if c == ' ':
                ans += '%20'
            else:
                ans += c
        return ans