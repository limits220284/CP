class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        for i in range(n-1):
            if nums[i+1]<=nums[i]:
                pre=nums[i+1]
                nums[i+1]=nums[i]+1
                res+=(nums[i+1]-pre)
        return res