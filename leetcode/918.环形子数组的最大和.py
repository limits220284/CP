#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 1)
        ans = -inf
        for i in range(1, n+1):
            f[i] = max(nums[i-1], f[i-1] + nums[i-1])
            ans = max(ans, f[i])
        r = 0
        l = sum(nums)
        mx = -inf
        for i in range(n-1, -1, -1):
            l -= nums[i]
            r += nums[i]
            mx = max(mx, r)
            ans = max(ans, mx + l)
        return ans
