#
# @lc app=leetcode.cn id=1761 lang=python3
#
# [1761] 一个图中连通三元组的最小度数
#

# @lc code=start
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # 暴力枚举三个点，然后判断是否能够构成三元组，然后计算入度即可
        IN = [0] * n
        g = [[False] * n for _ in range(n)]
        for x, y in edges:
            x -= 1; y -= 1
            g[x][y] = True
            g[y][x] = True
            IN[x] += 1
            IN[y] += 1
        ans = inf
        for x in range(n):
            for y in range(x+1, n):
                if g[x][y] == False: continue
                for z in range(y+1, n):
                    if g[y][z] == False: continue
                    if g[x][z]:
                        if IN[x] + IN[y] + IN[z] - 6 <  ans: ans = IN[x] + IN[y] + IN[z] - 6
        return ans if ans != inf else -1    
                    