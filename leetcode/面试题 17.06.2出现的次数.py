class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        s = str(n)
        @cache
        def f(i, cnt2, is_limit,is_num) -> int:
            if i == len(s):
                return cnt2
            res = 0
            if not is_num:
                res+=f(i+1,cnt2,False,False)
            up = int(s[i]) if is_limit else 9
            for d in range(1-int(is_num),up + 1):  # 枚举要填入的数字 d
                res += f(i + 1, cnt2 + (d == 2), is_limit and d == up,True)
            return res
        return f(0, 0, True,False)