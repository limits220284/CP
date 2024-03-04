class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        #二维动态规划，第一维表示步数，第二维表示位置
        #步数是根据k来确定，位置可以根据数据范围来进行确定
        N=2010
        Mod=1e9+7
        startPos+=500
        endPos+=500
        dp=[[0 for i in range(N)] for j in range(k+1)]
        dp[0][startPos]=1
        for i in range(1,k+1):
            for j in range(N):
                if j:dp[i][j]=dp[i-1][j-1]#j=startpos+1,该位置的步数可以从startpos转移过来，也可以从startpos+2转移过来
                if j<N-1:dp[i][j]=(dp[i][j]+dp[i-1][j+1])%Mod#
        return int(dp[k][endPos])
        