class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp=[1]*5
        i=1
        while i<=n:
            for j in range(3,-1,-1):
                dp[j]=dp[j]+dp[j+1]
            i+=1
        return dp[0]