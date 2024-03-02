class Solution:
    def sortVowels(self, s: str) -> str:
        ans = sorted([c for c in s if c in 'aeiouAEIOU'])
        j = 0
        s = list(s)
        for i, c in enumerate(s):
            if c in 'aeiouAEIOU':
                s[i] = ans[j]
                j += 1
        return "".join(s)