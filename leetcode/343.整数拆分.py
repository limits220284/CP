class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        arr=[]
        while n:
            if n>3:
                arr.append(3)
                n-=3
            else:
                arr.append(n)
                n-=n
        if arr[-1]==1:
            arr[-1]=arr[-2]=2
        return reduce(lambda x,y:x*y,arr)
        