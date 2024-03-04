class Solution:
    def reformat(self, s: str) -> str:
        sumDigit = sum(c.isdigit() for c in s)
        sumAlpha = len(s) - sumDigit
        if abs(sumDigit - sumAlpha) > 1:
            return ""
        flag = sumDigit > sumAlpha
        t = list(s)
        j = 1
        for i in range(0, len(t), 2):
            if t[i].isdigit() != flag:
                while t[j].isdigit() != flag:
                    j += 2
                t[i], t[j] = t[j], t[i]
        return ''.join(t)