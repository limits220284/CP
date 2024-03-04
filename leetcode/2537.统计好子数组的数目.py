class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        #枚举左端点，然后计算右端点
        #每次枚举的时候用dic统计出现过的数字然后加上即可
        #左端点
        n=len(nums)
        ans=0
        l,r=0,0
        t=0
        dic=defaultdict(int)
        while l<n:
            while r<n and t<k:
                if nums[r] not in dic or dic[nums[r]]==0:
                    dic[nums[r]]+=1
                else:
                    t+=dic[nums[r]]
                    dic[nums[r]]+=1
                r+=1
            if t>=k:
                ans+=n-r+1
            # 删除左端点
            if nums[l] in dic:
                tp=dic[nums[l]]
                if tp==1:
                    dic[nums[l]]-=1
                else:
                    dic[nums[l]]-=1
                    t-=tp-1
            l+=1
        return ans
                
                        