class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        inx=[1,-1,0,0]
        iny=[0,0,-1,1]
        cnt=0
        def dfs(x,y):
            nonlocal cnt
            vis[x][y]=1
            j=4
            for i in range(4):
                dx,dy=x+inx[i],y+iny[i]
                if dx>=0 and dx<m and dy>=0 and dy<n:
                    if grid[dx][dy]==1 and vis[dx][dy]==0:
                        dfs(dx,dy)
                        j-=1
                    elif grid[dx][dy]==1 and vis[dx][dy]==1:
                        j-=1
            print(j)
            cnt+=j

        m,n=len(grid),len(grid[0])
        vis=[[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    dfs(i,j)
                    return cnt
        return cnt
