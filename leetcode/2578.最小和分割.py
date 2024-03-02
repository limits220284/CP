class Solution:
    def splitNum(self, num: int) -> int:
        num = [c for c in str(num)]
        num.sort()
        odd = []
        even = []
        for i, c in enumerate(num):
            if i % 2:
                odd.append(c)
            else:
                even.append(c)
        return int("".join(odd)) + int("".join(even))