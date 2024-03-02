#
# @lc app=leetcode.cn id=980 lang=python3
#
# [980] 不同路径 III
#

# @lc code=start
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # 将所有的为零的空格拿出来，然后进行二进制枚举，并验证每一条路是否正确即可
        # 2**20**20
        ans = 0
        m, n = len(grid), len(grid[0])
        inx = [0, 0, -1, 1]
        iny = [1, -1, 0, 0]
        def dfs(x, y, cnt):
            nonlocal ans
            if grid[x][y] == 2 and cnt == 1:
                ans += 1
                return
            if cnt == 1:
                return
            t = grid[x][y]
            grid[x][y] = -1
            for k in range(4):
                dx, dy = x + inx[k], y + iny[k]
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] != -1:
                    dfs(dx, dy, cnt - 1)
            grid[x][y] = t

        x, y = 0, 0
        cnt0 = 0
        for i in range(m):
            for j in range(n):
                # 统计零的个数
                if grid[i][j] == 1:
                    x, y = i, j
                if grid[i][j] != -1:
                    cnt0 += 1
        dfs(x, y, cnt0)
        return ans
        
