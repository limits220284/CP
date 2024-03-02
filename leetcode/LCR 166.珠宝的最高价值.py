class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        v=[[0]*n for _ in range(m)]
        v[0][0]=grid[0][0]
        for i in range(1,m):
            v[i][0]=v[i-1][0]+grid[i][0]
        for j in range(1,n):
            v[0][j]=v[0][j-1]+grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                v[i][j]=max(v[i-1][j],v[i][j-1])+grid[i][j]
        return v[m-1][n-1]
        
        
