class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        inx=[1,-1,0,0]
        iny=[0,0,-1,1]
        n=len(grid)
        cnt=0
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    continue
                cnt+=2
                for k in range(4):
                    dx,dy=i+inx[k],j+iny[k]
                    if dx>=0 and dy>=0 and dx<n and dy<n:
                        if grid[dx][dy]>=grid[i][j]:
                            cnt+=0
                        else:
                            cnt+=(grid[i][j]-grid[dx][dy])
                    else:
                        cnt+=grid[i][j]
        return cnt           