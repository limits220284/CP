#
# @lc app=leetcode.cn id=646 lang=python3
#
# [646] 最长数对链
#

# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        f = [1] * n
        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    f[i] = max(f[i], f[j]+1)
        return max(f)

                

