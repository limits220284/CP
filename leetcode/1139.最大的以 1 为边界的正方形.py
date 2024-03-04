class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        up = [[0]*n for _ in range(m+1)]
        left = [[0]*(n+1) for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    up[i+1][j] = up[i][j] + 1
                    left[i][j+1] = left[i][j] + 1
                for l in range(min(i,j)+1,0,-1):
                    if l * l <= ans:
                        break
                    if up[i+1][j]>=l and left[i][j+1]>=l and left[i-l+1][j+1]>=l and up[i+1][j-l+1]>=l:
                        ans=max(ans,l)
        # 枚举正方形的边长
        return ans**2