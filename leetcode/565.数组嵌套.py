class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n=len(nums)
        mx=0
        vis=[False for _ in range(n)]
        for i in range(n):
            if vis[i]:
                continue
            j=nums[i]#j=0
            
            vis[j]=True
            cnt=1
            while j!=i:
                cnt+=1
                j=nums[j]# 5 6 2 
                vis[j]=True
            mx=max(mx,cnt)
        return mx