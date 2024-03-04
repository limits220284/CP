class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        mx=0
        m,n=len(grid),len(grid[0])
        for i in range(2,m):
            for j in range(2,n):
                mx=max(mx,grid[i][j]+grid[i][j-1]+grid[i][j-2]+grid[i-1][j-1]+grid[i-2][j]+grid[i-2][j-1]+grid[i-2][j-2])
        return mx