class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        print(m,n)
        if k>=m*n:
            k=k%(m*n)
        print(k)
        ans=[]
        _k=m*n-k
        while _k<m*n:
            ans.append(grid[_k//n][_k%n])
            _k+=1
        for i in range(m*n-k-1,-1,-1):
            x=i+k
            grid[x//n][x%n]=grid[i//n][i%n]
        for i in range(k):
            grid[i//n][i%n]=ans[i]
        return grid
            
            