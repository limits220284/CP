DIFFS = (0, 0, 1, -1, -1, 1, 1, -1, 0, 1)

class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = str(n)
        @cache
        def f(i: int, has_diff: bool, is_limit: bool) -> int:
            if i == len(s):
                return has_diff  # 只有包含 2/5/6/9 才算一个好数
            res = 0
            up = int(s[i]) if is_limit else 9
            for d in range(0, up + 1):  # 枚举要填入的数字 d
                if DIFFS[d] != -1:  # d 不是 3/4/7
                    res += f(i + 1, has_diff or DIFFS[d], is_limit and d == up)
            return res
        return f(0, False, True)