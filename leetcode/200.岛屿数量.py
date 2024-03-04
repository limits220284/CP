class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        inx=[1,-1,0,0]
        iny=[0,0,1,-1] 
        m,n=len(grid),len(grid[0])

        def dfs(x,y):
            for i in range(4):
                dx,dy=x+inx[i],y+iny[i]
                if dx>=0 and dx<m and dy>=0 and dy<n:
                    if grid[dx][dy]=='1':
                        grid[dx][dy]='#'
                        dfs(dx,dy)
       
        cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    grid[i][j]='#'
                    cnt+=1
                    dfs(i,j)
        return cnt
                
                
        