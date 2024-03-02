class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        idx = 0
        sign = 1
        while idx < n and s[idx] == ' ':
            idx += 1
        if idx < n and (s[idx] == '-' or s[idx] == '+'):
            sign = -1 if s[idx] == '-' else 1
            idx += 1
        ans = 0
        while idx < n and s[idx].isdigit():
            t = ord(s[idx]) - ord('0')
            if ans >= (2 ** 31 - t) / 10:
                return 2 ** 31 - 1 if sign == 1 else -2 ** 31
            ans = ans * 10 + t
            idx += 1
        return ans * sign
