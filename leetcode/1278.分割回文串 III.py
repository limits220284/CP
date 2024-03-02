class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        # 定义动态规划方程
        # f[i][j] 为a[0-i] 成为j段所需要的最小修改次数
        # f[i][j] = f[i-1][j-1] + 0, f[i-2][j-1] + 将该段搞成回文串最小修改次数
        n = len(s)

        dp = [[0]*n for _ in range(n)]
        # 预处理cost，代表将a[i-j]搞成回文串的最少次数
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = dp[i+1][j-1] + 1 - int(s[i] == s[j])
        
        f = [[inf] * (k+1) for _ in range(n+1)]
        f[0][0] = 0
        for i in range(1, n+1):
            for j in range(1, min(k, i) + 1):
                for t in range(j-1, i):
                    f[i][j] = min(f[i][j], f[t][j-1] + dp[t][i-1])
        return f[-1][-1]