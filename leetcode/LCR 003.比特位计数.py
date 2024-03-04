class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]
        highbit=0
        for i in range(1,n+1):
            if i&(i-1)==0:
                highbit=i
            dp.append(1+dp[i-highbit])
        return dp