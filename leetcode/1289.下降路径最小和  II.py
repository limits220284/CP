class Solution:
    def minFallingPathSum1(self, grid: List[List[int]]) -> int:
        n = len(grid)
        f = [[inf] * n for _ in range(n)]
        for i in range(n): f[0][i] = grid[0][i]
        for i in range(1, n):
            for j in range(n):
                for t in range(n):
                    if t == j: continue
                    f[i][j] = min(f[i][j], f[i-1][t] + grid[i][j])
        return min(f[-1]) 
        # 可以通过维护上一行的最小值和次小值将复杂度降到n**2
        # 具体是因为当前行状态的转移至用到了上一行的最小值和次小值
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        fir, sec = (inf, -1), (inf, -1)
        for i in range(n):
            if grid[0][i] < fir[0]:
                sec = fir
                fir = (grid[0][i], i)
            elif grid[0][i] == fir[0]:
                sec = (fir[0], i)
            elif grid[0][i] < sec[0]:
                sec = (grid[0][i], i)
        for i in range(1, n):
            curfir, cursec = (inf, -1), (inf, -1)
            cur_min = inf
            for j in range(n):
                if j != fir[1]:
                    cur_min = fir[0] + grid[i][j]
                else:
                    cur_min = sec[0] + grid[i][j]
                if cur_min < curfir[0]:
                    cursec = curfir
                    curfir = (cur_min, j)
                elif cur_min == curfir[0]:
                    cursec = (curfir[0], j)
                elif cur_min < cursec[0]:
                    cursec = (cur_min, j)
            fir, sec = curfir, cursec
        return fir[0]
                    
                
