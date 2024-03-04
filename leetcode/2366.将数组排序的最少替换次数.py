class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n=len(nums)
        nxt=nums[n-1]
        res=0
        for i in range(n-2,-1,-1):
            if nums[i]>nxt:
                k=math.ceil(nums[i]/nxt)
                res+=k-1
                nxt=nums[i]//k
            else:
                nxt=nums[i]
        return res
                
                