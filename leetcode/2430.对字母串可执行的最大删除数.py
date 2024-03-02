class Solution:
    def deleteString(self, s: str) -> int:
        # 定义f[i]表示删除后缀s[i:]所需要的最大操作数
        # f[i] = f[i+j:] if s[i: i + j] == s[i + j: i + 2j]
        # f[i] = 1
        # 取max
        # 但是这个s[i: i + j] == s[i + j: i + 2j]是否相等应该如何计算呢？
        if len(set(s)) == 1: return len(s)
        n = len(s)
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if s[i] == s[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1
        n = len(s)
        f = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(1, (n - i) // 2 + 1):
                if lcp[i][i + j] >= j:
                    f[i] = max(f[i], f[i + j] + 1)
        return f[0]