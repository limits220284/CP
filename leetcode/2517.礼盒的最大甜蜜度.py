class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        # 存在这种单调性的一般都可以使用二分法进行求解
        price.sort()
        n=len(price)
        def check(mid):
            cnt=1
            x0=price[0]
            for i in range(1,n):
                if price[i]>=x0+mid:
                    cnt+=1
                    x0=price[i]
            return cnt>=k
        l,r=0,(price[-1]-price[0])//(k-1)
        while l<r:
            mid=(l+r+1)//2
            if check(mid):
                l=mid
            else:
                r=mid-1
        return l
