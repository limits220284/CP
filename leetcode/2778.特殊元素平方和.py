class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i, x in enumerate(nums):
            if n % (i+1) == 0:
                ans += nums[i] ** 2
        return ans