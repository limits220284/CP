#
# @lc app=leetcode.cn id=1463 lang=python3
#
# [1463] 摘樱桃 II
#

# @lc code=start
class Solution:
    # 状态空间搜索解法
    def cherryPickup1(self, grid: List[List[int]]) -> int:
        # 需要给每个格子都标记一个状态, 状态搜索？
        # 广度优先搜索，状态存放为(i, j1, j2, tot)
        m, n = len(grid), len(grid[0])
        q = deque([(0, 0, n-1)])
        ans = 0
        vis = {}
        vis[(0, 0, n-1)] = grid[0][0] + grid[0][n-1]
        while q:
            tot = len(q)
            for i in range(tot):
                x, y1, y2 = q.popleft()
                if x == m-1:
                    ans = max(ans, vis[(x, y1, y2)])
                x1 = x + 1
                for ya in [y1 - 1, y1, y1 + 1]:
                    for yb in [y2 - 1, y2, y2 + 1]:
                        if 0 <= x1 < m and 0 <= ya < n and 0 <= yb < n and ya != yb:
                            if (x1, ya, yb) not in vis:
                                vis[(x1, ya, yb)] = vis[(x, y1, y2)] + grid[x1][ya] + grid[x1][yb]
                                q.append((x1, ya, yb))
                            else:
                                vis[(x1, ya, yb)] = max(vis[(x, y1, y2)] + grid[x1][ya] + grid[x1][yb], vis[(x1, ya, yb)])
        return ans
    # 
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # 动态规划解法
        # f[i][j][k]代表当前处于i层，两个机器人处于j, k位置樱桃的最大值
        m, n = len(grid), len(grid[0])
        f = [[[-inf] * n for  _ in range(n)] for _ in range(m)]
        f[0][0][n-1] = grid[0][0] + grid[0][n-1]
        for x1 in range(m-1):
            for y1 in range(n):
                for y2 in range(n):
                    if y1 == y2: continue
                    # 用当前的位置推理下面的位置，刷表法
                    x2 = x1 + 1
                    for ya in [y1 - 1, y1, y1 + 1]:
                        for yb in [y2 - 1, y2, y2 + 1]:
                            if ya == yb:continue
                            if 0 <= x2 < m and 0 <= ya < n and 0 <= yb < n and ya != yb:           
                                f[x2][ya][yb] = max(f[x2][ya][yb], f[x1][y1][y2] + grid[x2][ya] + grid[x2][yb])
        ans = 0
        for i in range(n):
            for j in range(n):
                if i == j: continue
                ans = max(ans, f[m-1][i][j])
        return ans               

