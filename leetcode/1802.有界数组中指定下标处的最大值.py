class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        #二分+贪心
        def check(mid):
            tot=mid
            l=index
            r=n-index-1
            tot+= mid*(mid-1)//2+(r-mid+1) if r>=mid-1 else (2*mid-1-r)*r//2
            tot += mid*(mid-1)//2+(l-mid+1) if l>=mid-1 else (2*mid-1-l)*l//2
            return tot<=maxSum
        l,r=0,maxSum
        while l<r:
            mid=(l+r+1)//2
            if check(mid):
                l=mid
            else:
                r=mid-1
        return l
