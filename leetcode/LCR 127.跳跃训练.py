class Solution:
    def numWays(self, n: int) -> int:
        a,b,c=1,1,0
        if n<=1:
            return 1
        for i in range(2,n+1):
            c=(a+b)%(1e9+7)
            a=b
            b=c
        return int(c)