#
# @lc app=leetcode.cn id=1345 lang=python3
#
# [1345] 跳跃游戏 IV
#

# @lc code=start
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # 先把相同元素的下标加到一起
        dic = defaultdict(list)
        for i, x in enumerate(arr):
            dic[x].append(i)
        vis = [False] * n
        q = deque([0])
        dep = 0
        while q:
            m = len(q)
            for i in range(m):
                t = q.popleft()
                if t == n-1: return dep
                if t < n-1 and not vis[t+1]:
                    vis[t+1] = True
                    q.append(t+1)
                if t > 0 and not vis[t-1]:
                    vis[t-1] = True
                    q.append(t-1)
                for x in dic[arr[t]]:
                    vis[x] = True
                    q.append(x)
                del dic[arr[t]]
            dep += 1
        return -1

