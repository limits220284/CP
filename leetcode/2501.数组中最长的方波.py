class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        n=len(nums)
        dic=Counter(nums)
        res=-1
        for x in nums:
            t=x
            cnt=0
            while x in dic:
                x=x**2
                cnt+=1
            if cnt>1:
                res=max(res,cnt)
        return res
            