class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        le,lo=0,0
        re,ro=0,0
        for i in range(n):
            if i%2==0:
                re+=nums[i]
            else:
                ro+=nums[i]
        for i in range(n):
            if i%2==0:
                re-=nums[i]
                if re+lo==ro+le:
                    ans+=1
                le+=nums[i]
            else:
                ro-=nums[i]
                if ro+le==re+lo:
                    ans+=1
                lo+=nums[i]
        return ans
