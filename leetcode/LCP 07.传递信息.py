class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        dp=[[0 for _ in range(n)] for i in range(k+1)]
        dp[0][0]=1
        for cnt in range(1,k+1):
            for i,j in relation:
                dp[cnt][j]+=dp[cnt-1][i]
        return dp[k][n-1]