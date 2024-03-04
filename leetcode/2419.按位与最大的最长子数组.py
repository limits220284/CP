class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx=max(nums)
        # 直接看一下mx能够持续多长即可
        ans=0
        cnt=0
        for i,x in enumerate(nums):
            if x==mx:
                cnt+=1
            else:
                ans=max(ans,cnt)
                cnt=0
        return max(ans,cnt)
        