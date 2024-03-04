class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        s=sum(nums)
        nums.sort()
        n=len(nums)
        res=[]
        um=0
        for i in range(n-1,-1,-1):
            if s-um>=um:
                um+=nums[i]
                res.append(nums[i])
        return res