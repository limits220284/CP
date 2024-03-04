class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # #双指针O(n)解法
        # l,r=0,0
        # n=len(nums)
        # tot=0
        # ans=n+1
        # while r<n:
        #     tot+=nums[r]
        #     while tot>=target:
        #         ans=min(ans,r-l+1)
        #         tot-=nums[l]
        #         l+=1
        #     r+=1
        # return ans if ans!=n+1 else 0
        # 二分解法
        n=len(nums)
        def check(mid):
            tot=0
            l=0
            while l<n:
                if l<mid-1:
                    tot+=nums[l]
                    l+=1
                    continue
                tot+=nums[l]
                if tot>=target:
                    return True
                tot-=nums[l-mid+1]
                l+=1
            return False

        l,r=1,n+1
        while l<r:
            mid=(l+r)//2
            if check(mid):
                r=mid
            else:
                l=mid+1
        return 0 if l==n+1 else l






