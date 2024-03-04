class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        cnt=0
        vis=[False]*(right+1)
        prime=[]
        def f_prime(n):
            nonlocal cnt
            for i in range(2,n+1):
                if not vis[i]:
                    prime.append(i)
                    cnt+=1
                    j=i
                    while j<=n:
                        vis[j]=True
                        j+=i

        f_prime(right)
        prime=[x for x in prime if x>=left]
        dx,dy=-1,-1
        mi=1e9
        for x,y in pairwise(prime):
            if y-x<mi:
                dx,dy=x,y
                mi=y-x
        return [dx,dy]
        