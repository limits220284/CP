class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n=len(grid)
        row=[0]*n
        col=[0]*n
        for i in range(n):
            for j in range(n):
                row[i]=max(grid[i][j],row[i])
                col[j]=max(grid[i][j],col[j])
        cnt=0
        for i in range(n):
            for j in range(n):
                cnt+=min(row[i],col[j])-grid[i][j]
        return cnt
        