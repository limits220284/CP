class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10 ** 9 + 7
        def work(s):
            @cache
            def f(i, pre, is_limit, is_num):
                if i == len(s):
                    return int(is_num)
                res = 0
                if not is_num:
                    res += f(i+1, pre, False, False)
                up = int(s[i]) if is_limit else 9
                for d in range(1-int(is_num), up+1):
                    if (is_num == False or abs(pre - d) == 1):
                        res = (res + f(i+1, d, is_limit and d == up, True)) % MOD
                return res
            return f(0, 0, True, False)
        k = 1
        n = len(low)
        for i in range(1, n):
            if abs(int(low[i]) - int(low[i-1])) != 1:
                k = 0
                break
        return (work(high) - work(low) + k) % MOD