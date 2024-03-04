class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 就是选择最大的两个数
        f,s=0,0
        for x in nums:
            if f<x:
                s=f
                f=x
            elif x>s:
                s=x
        return (f-1)*(s-1)