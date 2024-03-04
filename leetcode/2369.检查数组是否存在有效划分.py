class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(1,n):
            if dp[i-1] and nums[i]==nums[i-1]:
                dp[i+1]=True
            if i>1 and dp[i-2] and nums[i]==nums[i-1]==nums[i-2]:
                dp[i+1]=True
            if i>1 and dp[i-2] and nums[i]==nums[i-1]+1 and nums[i-1]==nums[i-2]+1:
                dp[i+1]=True
        return dp[n]