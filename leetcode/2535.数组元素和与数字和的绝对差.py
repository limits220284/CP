class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a=0
        b=sum(nums)
        for x in nums:
            while x:
                a+=x%10
                x//=10
        return abs(a-b)