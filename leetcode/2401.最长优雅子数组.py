class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        i,j,tot=0,0,0
        cnt=[0]*30
        ans=0
        while j<n:
            for k in range(30):
                if nums[j]>>k&1:
                    cnt[k]+=1
                if cnt[k]>1:
                    tot+=1
            while tot:
                for k in range(30):
                    if nums[i]>>k&1:
                        cnt[k]-=1
                        if cnt[k]==1:
                            tot-=1
                i+=1
            ans=max(ans,j-i+1)
            j+=1
        return ans