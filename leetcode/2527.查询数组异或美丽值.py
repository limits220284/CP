class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        ans=0
        for x in nums:
            ans=ans^x
        return ans