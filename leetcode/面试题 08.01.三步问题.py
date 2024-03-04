class Solution:
    def waysToStep(self, n: int) -> int:
        a,b,c=1,1,2
        if n<=2:
            return n
        t=0
        for i in range(3,n+1):
            t=(a+b+c)%1000000007
            a=b
            b=c
            c=t
        return t
        