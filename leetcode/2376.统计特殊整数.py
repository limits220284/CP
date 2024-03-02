class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        # 数位dp
        s = str(n)
        @cache
        def dfs(i, mask, is_limit, is_num): # i当前进行到第几位，mask 用来记录某个数是否被用过，is_limit前面是否被限制住，is_num前面是否填了数字
            if i == len(s):
                return int(is_num)
            res = 0
            # 跳过(只有前面不填数字才能跳过)
            if not is_num:
                res += dfs(i + 1, mask, False, is_num)
            # 不跳过
            up = int(s[i]) if is_limit else 9
            for d in range(1 - int(is_num), up + 1):
                if (mask >> d) & 1: continue
                res += dfs(i + 1, mask | (1 << d), d == up and is_limit, True)
            return res
        return dfs(0, 0, True, False)