class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx=nums[::]
        mi=nums[::]
        n=len(nums)
        for i in range(1,n):
            mx[i]=max(mx[i-1]*nums[i],mi[i-1]*nums[i],nums[i])
            mi[i]=min(mx[i-1]*nums[i],mi[i-1]*nums[i],nums[i])
        return max(mx)