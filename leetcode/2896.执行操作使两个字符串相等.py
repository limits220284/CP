"""
1、记忆化搜索方法
j表示方式1发生了多少次的反转
pre_rev表示前面是否发生了反转
"""
class Solution:
    def minOperations1(self, s1: str, s2: str, x: int) -> int:
        if s1.count('1') % 2 != s2.count("1") % 2:
            return -1
        @cache
        def dfs(i: int, j: int, pre_rev: bool) -> int:
            if i < 0:
                if j > 0 or pre_rev:
                    return inf
                return 0
            if not pre_rev:
                if s1[i] == s2[i]:
                    return dfs(i-1, j, False)
            else:
                if s1[i] != s2[i]:
                    return dfs(i-1, j, False)
            res1 = dfs(i-1, j+1, False) + x
            res2 = dfs(i-1, j, True) + 1
            res3 = inf
            if j > 0:
                res3 = dfs(i-1, j-1, False)
            return min(res1, res2, res3)
        return dfs(len(s1)-1, 0, False) 
    def minOperations2(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        p = []
        for i in range(n):
            if s1[i] != s2[i]:
                p.append(i)
        m = len(p)
        if m == 0: return 0
        if m % 2: return -1
        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            res1 = dfs(i-1) + x / 2
            res2 = dfs(i-2) + p[i] - p[i-1] if i > 0 else inf
            return min(res1, res2)
        return int(dfs(m-1))
    def minOperations3(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        p = []
        for i in range(n):
            if s1[i] != s2[i]:
                p.append(i)
        m = len(p)
        if m == 0: return 0
        if m % 2: return -1
        f = [0] * (m + 1)
        f[0] = 0
        f[1] = x
        for i in range(1, m):
            f[i+1] = min(f[i] + x, f[i-1] + (p[i] - p[i-1]) * 2)
        return f[m] // 2
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        p = []
        for i in range(n):
            if s1[i] != s2[i]:
                p.append(i)
        m = len(p)
        if m == 0: return 0
        if m % 2: return -1
        f0, f1 = 0, x
        for i in range(1, m):
            new = min(f1 + x, f0 + (p[i] - p[i-1]) * 2)
            f0 = f1
            f1 = new
        return f1 // 2
