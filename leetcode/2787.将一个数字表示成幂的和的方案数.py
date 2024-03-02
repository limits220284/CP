class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # 动态规划？
        arr = []
        i = 1
        while i ** x <= n:
            arr.append(i ** x)
            i += 1
        m = len(arr)
        f = [[0] * (n+1) for _ in range(m+1)]
        f[0][0] = 1
        for i in range(1, m+1):
            for j in range(n+1):
                f[i][j] = f[i - 1][j]
                if (j >= arr[i-1]): f[i][j] += f[i - 1][j - arr[i-1]]
        return f[m][n] % (10**9+7)