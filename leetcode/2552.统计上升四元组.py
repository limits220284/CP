class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n=len(nums)
        great=[0]*n
        great[-1]=[0]*(n+1)
        for k in range(n-2,-1,-1):
            great[k]=great[k+1][::]
            for x in range(1,nums[k+1]):
                great[k][x]+=1
        less=[0]*n
        less[0]=[0]*(n+1)
        for j in range(1,n-1):
            less[j]=less[j-1][::]
            for x in range(nums[j-1]+1,n+1):
                less[j][x]+=1
        # 枚举j和k
        ans=0
        for j in range(1,n-2):
            for k in range(j+1,n-1):
                if nums[j]>nums[k]:
                    ans+=less[j][nums[k]]*great[k][nums[j]]
        return ans