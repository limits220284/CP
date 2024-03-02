class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        m = 1 << len(cookies)
        # 预处理出来所有子集的和
        s = [0] * m
        for i in range(1, m):
            s[i] = s[i^i&-i] + cookies[(i&-i).bit_length()-1]
        # i表示前i个人,下标从零开始
        # f[i][j] = min(f[i-1][j\s], sum[s])
        f = [[0] * m for _ in range(k)]
        for i in range(m):
            f[0][i] = s[i]
        for i in range(1, k):
            for j in range(1, m):
                t = inf
                sub = j
                while sub:
                    t = min(t, max(s[sub], f[i-1][j ^ sub]))
                    sub = (sub - 1) & j
                f[i][j] = t
        return f[k-1][m-1]
