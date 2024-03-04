class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res=[[0 for i in range(n)] for j in range(n)]
        vis=[[False for i in range(n)] for j in range(n)]
        inx=[0,1,0,-1]
        iny=[1,0,-1,0]
        x,y=0,0
        i=0
        circle=0
        res[x][y]=1
        vis[x][y]=True
        cnt=2
        while cnt<=n**2:
            if circle==4:
                i+=circle/4
                circle=0
            dx,dy=x+inx[circle],y+iny[circle]
            while dx>=i and dx<n-i and dy>=i and dy<n-i and vis[dx][dy]==False:
                res[dx][dy]=cnt
                cnt+=1
                vis[dx][dy]=True
                x,y=dx,dy
                dx,dy=x+inx[circle],y+iny[circle]
            circle+=1
        return res
                
                
                
                
            