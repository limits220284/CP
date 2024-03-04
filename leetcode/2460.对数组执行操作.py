class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n-1):
            if nums[i]!=nums[i+1]:
                continue
            else:
                nums[i]=nums[i]*2
                nums[i+1]=0
        res=[0]*(n)
        t=0
        for x in nums:
            if x!=0:
                res[t]=x
                t+=1
        return res
            