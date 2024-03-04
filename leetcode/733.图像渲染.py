class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newcolor: int) -> List[List[int]]:
        inx=[1,-1,0,0]
        iny=[0,0,1,-1]
        def dfs(x,y):
            image[x][y]=newcolor
            for i in range(4):
                dx,dy=x+inx[i],y+iny[i]
                if dx>=0 and dx<m and dy>=0 and dy<n and image[dx][dy]==color:
                    dfs(dx,dy)

        m,n=len(image),len(image[0])
        color=image[sr][sc]
        if newcolor!=color:
            dfs(sr,sc)
        return image
