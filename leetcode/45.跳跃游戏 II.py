#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        q = deque()
        q.append(0)
        vis = [False] * n
        dep = 0
        while q:
            m = len(q)
            for i in range(m):
                t = q.popleft()
                if t == n-1: return dep
                for k in range(t+1, t+nums[t]+1):
                    if k < n and vis[k] == False:
                        vis[k] = True
                        q.append(k)
            dep += 1
        return dep
                


