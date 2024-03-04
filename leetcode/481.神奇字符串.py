
s = [1, 2, 2]
i = 2
while len(s) < 100000:
    s += [s[-1] ^ 3] * s[i]
    i += 1

acc = list(accumulate((2 - c for c in s), initial=0))

class Solution:
    def magicalString(self, n: int) -> int:
        return acc[n]
