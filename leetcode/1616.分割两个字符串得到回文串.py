class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(a, b):
            n = len(a)
            left, right = 0, n-1
            while left < right and a[left] == b[right]:
                left += 1
                right -= 1
            if left >= right:
                return True
            s = a[left:right+1]
            t = b[left:right+1]
            return s == s[::-1] or t == t[::-1]
        return check(a, b) or check(b, a)