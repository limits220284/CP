class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[inf] * n for _ in range(m)]
        f[0] = grid[0]
        for i in range(m - 1):
            for j in range(n):
                for k in range(n):
                    f[i + 1][k] = min(f[i + 1][k], f[i][j] + moveCost[grid[i][j]][k] + grid[i + 1][k])
        print(f)
        return min(f[-1])
