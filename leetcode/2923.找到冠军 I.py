class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vis = set(range(n))
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if j in vis:
                        vis.remove(j)
        return list(vis)[0]