class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        i, n = 0, len(s)
        l0, l1 = 0, 0
        while i < n:
            start = i
            while i < n-1 and s[i] == s[i+1]:
                i += 1
            if s[start] == '0':
                l0 = max(l0, i - start + 1)
            else:
                l1 = max(l1, i - start + 1)
            i += 1
        return l1 > l0