class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        #异或之后查看哪些位置为零,然后将其补充上去即可
        dp=[0]
        n=len(nums)
        res=[]
        for i in range(n):
            dp.append(dp[i]^nums[i])
            res.append(dp[-1]^(2**maximumBit-1))
        res=res[::-1]
        return res
        
            