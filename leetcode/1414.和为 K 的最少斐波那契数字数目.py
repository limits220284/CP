class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # 考虑这么一个方案
        # 首先预处理出来小于1e9的f数
        # 选择最接近k的数,然后继续这样选择,直到结束
        # ?这种贪心思路是否正确
        # 假设找最大的是最好的,k=A+B,k=C+D
        # A>C,B<D
        # 预处理
        f=[1,1]
        while f[-1]+f[-2]<=k:
            f.append(f[-1]+f[-2])
        l,r=0,len(f)-1
        cnt=0
        n=len(f)
        print(f)
        while k:
            l,r=0,n-1
            while l<r:
                mid=(l+r)//2
                if f[mid]>=k:
                    r=mid
                else:
                    l=mid+1
            if k>=f[l]:
                k-=f[l]
            else:
                k-=f[l-1]
            cnt+=1
        return cnt
        