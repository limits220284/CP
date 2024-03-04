class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # 二分的思路
        arr=[]
        for i,r in enumerate(ranges):
            arr.append((i-r,i+r))
        arr.sort(key=lambda x:(x[1],x[0]))
        t=n
        cnt=0
        up=n
        while t>0:
            l,r=0,n
            while l<r:
                mid=(l+r)//2
                if arr[mid][1]>=t:
                    r=mid
                else:
                    l=mid+1
            if arr[l][1]>=t:
                pre=t
                k=l
                mi=1e5
                while k<=up:
                    mi=min(mi,arr[k][0])
                    k+=1
                t=mi
                if t==pre:
                    return -1
                up=l
            else:
                return -1
            cnt+=1
        return cnt