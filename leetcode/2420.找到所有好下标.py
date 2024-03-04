class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        dec=[1]*(n)
        for i in range(n-2,k,-1):
            if nums[i]<=nums[i+1]:
                dec[i]=dec[i+1]+1
        inc=1
        ans=[]
        for i in range(1,n-k):
            if inc>=k and dec[i+1]>=k:
                ans.append(i)
            if nums[i]<=nums[i-1]:
                inc+=1
            else:
                inc=1
            
        return ans