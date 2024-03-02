#
# @lc app=leetcode.cn id=2151 lang=python3
#
# [2151] 基于陈述统计最多好人数
#

# @lc code=start
class Solution:               
    def maximumGood(self, statements: List[List[int]]) -> int:
        # 二进制枚举，然后看看所有的情况是否都满足
        n = len(statements)
        ans = 0
        for i in range(1 << n):
            flag = True
            for j, row in enumerate(statements):
                if i >> j & 1:
                    for k, st in enumerate(row):
                        if st != 2 and st != i >> k & 1:
                            flag = False
                            break
            if flag:
                ans = max(ans, bin(i).count('1'))
        return ans 
        
