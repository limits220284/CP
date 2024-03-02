#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key = lambda x: x[1])
        print(intervals)
        cur = -inf
        ans = 0
        for i, x in enumerate(intervals):
            if x[0] >= cur:
                cur = x[1]
            else:
                ans += 1
        return ans

