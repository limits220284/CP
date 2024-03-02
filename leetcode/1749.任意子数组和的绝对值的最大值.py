class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        # 直接动态规划
        # f[i] = max(abs(f[i-1] + nums[i], abs(nums[i]))
        f = [0] * n
        f[0] = nums[0]
        for i in range(1, n):
            f[i] = max(f[i-1] + nums[i], nums[i])
        ans = max(f)
        f = [0] * n
        f[0] = nums[0]
        for i in range(1, n):
            f[i] = min(f[i-1] + nums[i], nums[i])
        return max(ans, abs(min(f)))
            
            