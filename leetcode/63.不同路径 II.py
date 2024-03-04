class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        dp=[[0 for i in range(n)] for j in range(2)]
        dp[1][0]=1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    continue
                if j-1>=0:
                    dp[1][j]+=dp[1][j-1]
                if i-1>=0:
                    dp[1][j]+=dp[0][j]
            dp[0]=dp[1][:]
            dp[1]=[0 for i in range(n)]
        return dp[0][n-1]