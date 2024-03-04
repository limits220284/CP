class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 枚举右端点,然后统计符合性质的左端点的个数
        l,r=0,0
        n=len(nums)
        tot=1
        ans=0
        while r<n:
            if nums[r]>=k:
                r+=1
                l=r
                tot=1
                continue
            tot*=nums[r]
            while tot>=k:
                tot//=nums[l]
                l+=1
            ans+=r-l+1
            r+=1
        return ans