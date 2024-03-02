class Solution:
    def minInsertions(self, s: str) -> int:
        # 枚举中间这个字符，然后以该字符为中心，判断至少需要多少
        # f[i][j] 表示s[i-j]成为回文串所需要插入多少个
        # f[i][j] = f[i+1][j-1] if s[i] == s[j]
        # f[i][j] = min(f[i+1][j], f[i][j-1]) + 1
        # n = len(s)
        # f = [[0] * n for _ in range(n)]
        # for i in range(n-2, -1, -1):
        #     for j in range(i+1, n):
        #         f[i][j] = min(f[i+1][j], f[i][j-1]) + 1
        #         if s[i] == s[j]:
        #             f[i][j] = min(f[i][j], f[i+1][j-1])
        # return f[0][-1]
        t = s[::-1]
        n = len(s)
        f = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                f[i][j] = max(f[i-1][j], f[i][j-1])
                if s[i-1] == t[j-1]:
                    f[i][j] = f[i-1][j-1] + 1
        return n - f[-1][-1]