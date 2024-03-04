class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # 这种最大值最小的问题一般都可以采用二分的方法来写
        # 这个题就是将每个bag中的球数目作为上界，下界为1
        def check(x):
            cnt=0
            for y in nums:
                cnt+=(y-1)//x
            return cnt
        l,r=1,max(nums)
        while l<r:
            mid=(l+r)//2
            if check(mid)<=maxOperations:
                r=mid
            else:
                l=mid+1
        return l
        
                
                
