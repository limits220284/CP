class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # 定义f[i][j]为s1[0:i]和s2[0:j]相同的最小删除和
        # f[0][0] = 0
        # f[0][j] = f[0][j-1] + s2[j-1]
        # f[i][0] = f[i-1][0] + s1[i-1]
        # s1[i-1]=s2[j-1]: f[i][j] = f[i-1][j-1]
        # s1[i-1]!=s2[j-1]: f[i][j] = min(f[i-1][j] + s1[i-1], f[i][j-1] + s2[j-1])
        m, n = len(s1), len(s2)
        as1 = [ord(c) for c in s1]
        as2 = [ord(c) for c in s2]
        f = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, n+1): f[0][i] = f[0][i-1] + as2[i-1]
        for i in range(1, m+1): f[i][0] = f[i-1][0] + as1[i-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if as1[i-1] == as2[j-1]:
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = min(f[i-1][j] + as1[i-1], f[i][j-1] + as2[j-1])
        return f[-1][-1]
