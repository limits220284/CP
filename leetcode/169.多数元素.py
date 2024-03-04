class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        t=nums[0]
        n=len(nums)
        cnt=1
        for i in range(1,n):
            if nums[i]==t:
                cnt+=1
            else:
                cnt-=1
                if cnt==-1:
                    t=nums[i]
                    cnt=1
        return t