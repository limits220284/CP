class Solution:
    def averageValue(self, nums: List[int]) -> int:
        cnt=0
        tot=0
        for x in nums:
            if x%3==0 and x%2==0:
                cnt+=1
                tot+=x
        if cnt==0:
            return 0
        return tot//cnt