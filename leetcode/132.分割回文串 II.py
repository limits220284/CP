#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        ## 计算最少的分割次数
        ## f[i] 代表以i结尾的最小分割次数
        n = len(s)
        f = [[True] * (n+1) for _ in range(n+1)]
        for i in range(n, 0, -1):
            for j in range(i, n+1):
                if i + 1 > j-1: f[i][j] = (s[i-1] == s[j-1])
                else: f[i][j] = f[i+1][j-1] and (s[i-1] == s[j-1])
        dp = [inf] * (n+1)
        dp[0] = 0
        # f[i] = min(f[i], f[j] && isp(a[j:i]))
        for i in range(1, n+1):
            for j in range(1, i+1):
                if f[j][i] == True:
                    dp[i] = min(dp[i], dp[j-1] + 1)
        print(dp)
        return dp[n]-1

