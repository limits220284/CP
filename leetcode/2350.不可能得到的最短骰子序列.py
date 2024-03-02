#
# @lc app=leetcode.cn id=2350 lang=python3
#
# [2350] 不可能得到的最短骰子序列
#

# @lc code=start
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        # 贪心的进行匹配
        st = set()
        ans = 0
        for x in rolls:
            st.add(x)
            if len(st) == k:
                st.clear()
                ans += 1
        return ans + 1
        

