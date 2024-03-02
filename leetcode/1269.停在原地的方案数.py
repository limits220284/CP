class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # 动态规划解法
        # 考虑状态转移f[i][j]:代表经过i步之后到达位置j的方案数
        # 1、如果不动:f[i-1][j]
        # 2、如果从右边过来的:f[i-1][j+1]
        # 3、如果从左边过来的:f[i-1][j-1]
        # 4、总的方案数应该为:f[i][j] = f[i-1][j]+f[i-1][j+1]+f[i-1][j-1]
        # 5、考虑边界问题:f[0][any] = 0
        MOD = 10**9 + 7
        mx = min(steps // 2 + 1, arrLen)
        f = [0] * mx
        f[0] = 1
        for i in range(1, steps + 1):
            dp = [0] * mx
            for j in range(mx):
                dp[j] = f[j]
                if j:
                    dp[j] += f[j-1]
                if j+1 < mx:
                    dp[j] += f[j+1]
                dp[j] %= MOD
            f = dp
        return f[0]
                