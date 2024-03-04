class Solution:
    def __init__(self):
        self.cnt=0
        self.res=0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        inx=[0,0,1,-1]
        iny=[-1,1,0,0]
        def dfs(x,y):
            self.cnt+=1
            grid[x][y]=0
            for i in range(4):
                dx,dy=x+inx[i],y+iny[i]
                if dx>=0 and dx<m and dy>=0 and dy<n and grid[dx][dy]==1:
                    dfs(dx,dy)
                
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    self.cnt=0
                    dfs(i,j)
                    self.res=max(self.res,self.cnt)
        return self.res