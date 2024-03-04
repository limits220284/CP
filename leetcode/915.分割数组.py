class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        leftmax,mx=nums[0],nums[0]
        pos=0
        n=len(nums)
        for i in range(1,n):
            mx=max(mx,nums[i])
            if nums[i]>=leftmax:
                continue
            leftmax=mx
            pos=i
        return pos+1