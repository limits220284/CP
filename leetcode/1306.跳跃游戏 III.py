#
# @lc app=leetcode.cn id=1306 lang=python3
#
# [1306] 跳跃游戏 III
#

# @lc code=start
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = deque([start])
        vis = [False] * n
        while q:
            m = len(q)
            for i in range(m):
                t = q.popleft()
                if arr[t] == 0: return True
                for k in [t + arr[t], t - arr[t]]:
                    if 0 <= k < n and vis[k] == False:
                        vis[k] = True
                        q.append(k)
        return False
