class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def work(s):
            @cache
            def f(i, cnt, modk, is_limit, is_num):
                if i == len(s):
                    if cnt == 0 and modk % k == 0:
                        return int(is_num)
                    return 0
                res = 0
                if not is_num:
                    res += f(i+1, cnt, modk, False, False)
                up = int(s[i]) if is_limit else 9
                for d in range(1-int(is_num), up+1):
                    res = res + f(i+1, cnt + (1 if d % 2 == 1 else -1), (modk * 10 + d) % k, is_limit and d == up, True)
                return res
            return f(0, 0, 0, True, False)
        
        low, high= str(low-1), str(high)
        return work(high) - work(low)