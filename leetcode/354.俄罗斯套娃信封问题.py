#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        arr = [x[1] for x in envelopes]
        
        q = []
        for x in arr:
            l, r = 0, len(q) - 1
            while l < r:
                mid = (l + r) // 2
                if q[mid] >= x:
                    r = mid
                else:
                    l = mid + 1
            if not q or q[l] < x:
                q.append(x)
            else:
                q[l] = x
        return len(q)
                
