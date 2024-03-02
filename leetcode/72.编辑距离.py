#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        f = [[inf] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1+1): f[i][0] = i
        for i in range(n2+1): f[0][i] = i
        ## f[i][j] 增加，删除，替换
        for i in range(1,n1 + 1):
            for j in range(1, n2 + 1):
                f[i][j] = min(f[i-1][j] + 1, f[i][j-1] + 1)
                if word1[i-1] == word2[j-1]: f[i][j] = min(f[i][j], f[i-1][j-1])
                else: f[i][j] = min(f[i][j], f[i-1][j-1] + 1)
        return f[n1][n2]
