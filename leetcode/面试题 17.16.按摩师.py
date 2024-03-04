class Solution:
    def massage(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n<=2:
            return max(nums)
        nums[2]=nums[2]+nums[0]
        for i in range(3,n):
            nums[i]=max(nums[i]+nums[i-2],nums[i]+nums[i-3])
        return max(nums[n-1],nums[n-2])
        
            