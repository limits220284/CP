class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [-1] * (n + 2)

        for i in range(n):
            idx = nums[i] - 1
            dp[idx] = idx

        return [i+1 for i, x in enumerate(dp) if x == -1]
