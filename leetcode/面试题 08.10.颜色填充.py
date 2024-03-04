class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m,n=len(image),len(image[0])
        inx=[1,-1,0,0]
        iny=[0,0,1,-1]
        def dfs(x,y):
            image[x][y]=newColor
            for i in range(4):
                dx,dy=x+inx[i],y+iny[i]
                if dx>=0 and dx<m and dy>=0 and dy<n and image[dx][dy]==color:
                    dfs(dx,dy)
        color=image[sr][sc]
        if color==newColor:
            return image
        dfs(sr,sc)
        return image
        
            