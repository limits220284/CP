class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        #动态规划解法
        m,n=len(matrix),len(matrix[0])
        dp=[[0 for i in range(n)] for j in range(m)]
        sum=0
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=matrix[0][0]
                elif matrix[i][j]==0:
                    dp[i][j]=0
                elif i-1>=0 and j-1>=0:
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
                else:
                    dp[i][j]=matrix[i][j]
                sum+=dp[i][j]
        return sum