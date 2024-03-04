class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # 背包问题
        # dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+p[i])
        n=len(boxTypes)
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        cnt=0
        i=0
        res=0
        while i<n :
            if cnt+boxTypes[i][0]<=truckSize:
                cnt+=boxTypes[i][0]
                res+=boxTypes[i][1]*boxTypes[i][0]
            else:
                res+=(truckSize-cnt)*boxTypes[i][1]
                return res
            i+=1
        return res
                    