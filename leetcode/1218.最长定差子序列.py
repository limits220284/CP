#
# @lc app=leetcode.cn id=1218 lang=python3
#
# [1218] 最长定差子序列
#

# @lc code=start
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = Counter()
        for x in arr:
            dic[x] = dic[x - difference] + 1
        return max(dic.values())

