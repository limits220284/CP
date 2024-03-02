class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp[i] = max(dp[i-1], i + nums[i])
        n = len(nums)
        f = [0] * (n+1)
        for i in range(n):
            if i > f[i]: return False
            f[i+1] = max(f[i], i + nums[i])
        return True
            