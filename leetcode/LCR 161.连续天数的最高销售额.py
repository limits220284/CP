class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        for i in range(1,n):
            nums[i]=max(nums[i],nums[i]+nums[i-1])
        return max(nums)