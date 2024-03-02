class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        num1 = s.count('1')
        num0 = n - num1
        ans = []
        ans = ['1'] * (num1 - 1) + ['0'] * (num0) + ['1'] * 1
        return "".join(ans)