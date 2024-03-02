#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, a: List[int]) -> int:
        m = len(a)
        f = [0] * (amount + 1)
        f[0] = 1
        for i in range(1, m+1):
            for j in range(a[i-1], amount + 1):
                f[j] += f[j-a[i-1]]
        return f[amount]
