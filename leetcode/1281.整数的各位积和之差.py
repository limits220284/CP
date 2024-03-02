#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x = n
        pro = 1
        tot = 0
        while x:
            pro *= x % 10
            tot += x % 10
            # print(pro, tot)
            x //= 10
        return pro - tot

