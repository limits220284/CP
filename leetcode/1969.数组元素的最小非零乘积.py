#
# @lc app=leetcode.cn id=1969 lang=python3
#
# [1969] 数组元素的最小非零乘积
#

# @lc code=start
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        # 0的数量和1的数量是相同的
        MOD = 10 ** 9 + 7
        def qmd(a, k):
            res = 1
            while k:
                if k & 1:
                    res = res * a % MOD
                a = a * a % MOD
                k >>= 1
            return res
        x = 2 ** p - 2
        return qmd(x, x // 2) * (2 ** p - 1) % MOD
