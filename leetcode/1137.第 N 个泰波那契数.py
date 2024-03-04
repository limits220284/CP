class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        if n==2:
            return 1
        a,b,c,t=0,1,1,0
        for i in range(3,n+1):
            t=a+b+c
            a=b
            b=c
            c=t
        return t