class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #直接模拟
        res=[]
        m,n=len(matrix),len(matrix[0])
        vis=[[False for i in range(n)] for j in range(m)]
        inx=[0,1,0,-1]
        iny=[1,0,-1,0]
        circle=0
        i=0#圈数，circle 转满一圈i++
        cnt=1
        x,y=0,0
        res.append(matrix[x][y])
        vis[x][y]=True
        while cnt<m*n:
            if circle==4:
                i+=circle/4
                circle=0
            dx,dy=x+inx[circle],y+iny[circle]
            while dx>=i and dx<m-i and dy>=i and dy<n-i and vis[dx][dy]==False:
                res.append(matrix[dx][dy])
                cnt+=1
                vis[dx][dy]=True
                x,y=dx,dy
                dx,dy=x+inx[circle],y+iny[circle]
            circle+=1
        return res
        