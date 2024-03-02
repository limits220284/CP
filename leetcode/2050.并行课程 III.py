#
# @lc app=leetcode.cn id=2050 lang=python3
#
# [2050] 并行课程 III
#

# @lc code=start
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # 拓扑排序模版题
        g = [[] for _ in range(n)]
        q = deque()
        IN = [0] * n
        for x, y in relations:
            x -= 1
            y -= 1
            IN[y] += 1
            g[x].append(y)
        f = [0] * n
        for i, x in enumerate(IN):
            if x == 0:
                q.append(i)
                f[i] = time[i]
        while q:
            m = len(q)
            for i in range(m):
                t = q.popleft()
                for y in g[t]:
                    f[y] = max(f[y], f[t] + time[y])
                    IN[y] -= 1
                    if IN[y] == 0:
                        q.append(y)
        return max(f)