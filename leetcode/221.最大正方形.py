class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #动态规划解法
        m,n=len(matrix),len(matrix[0])
        dp=[[0 for i in range(n)] for j in range(2)]
        res=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='0':
                    dp[1][j]=0
                elif i-1>=0 and j-1>=0:
                    dp[1][j]=min(dp[1][j-1],dp[0][j],dp[0][j-1])+1
                else:
                    dp[1][j]=int(matrix[i][j])
                res=max(res,dp[1][j])
            dp[0]=dp[1]
            dp[1]=[0 for i in range(n)]
        return res**2