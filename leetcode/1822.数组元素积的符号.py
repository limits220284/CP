class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res=1
        for x in nums:
            if x==0:
                return 0
            res*= 1 if x>0 else -1
        return res
            