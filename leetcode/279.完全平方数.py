#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        # 完全背包模型
        # 问题等价于从[1,4,9,16,25,36]中任意选取某些数，使其结果等于n的最小数量
        # f[i][j]代表从前i个数中选择结果为j的最小数量
        # 不选a[i], f[i][j] = min(f[i-1][j])
        # 选a[i], f[i][j] = min(f[i-1][j-a[i]]+1, f[i-1][j - 2*a[i]]+2, ...)
        #         f[i][j-a[i]]+1 = min(f[i-1][j-2a[i]]+1, f[i-1][j-3a[i]]+2) 
        # f[i][j] = min(f[i][j-a[i]], f[i-1][j-a[i]])
        a = []
        i = 1
        while i*i <= n:
            a.append(i**2)
            i += 1
        m = len(a)
        f = [[inf] * (n+1) for _ in range(m+1)]
        for i in range(m+1): f[i][0] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                f[i][j] = f[i-1][j]
                if j >= a[i-1]:
                    f[i][j] = min(f[i-1][j], f[i][j-a[i-1]]+1, f[i-1][j-a[i-1]]+1)
        return f[m][n]
            

