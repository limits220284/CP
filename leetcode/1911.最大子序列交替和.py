class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # 买卖股票的最佳时机
        ans = nums[0]
        n = len(nums)
        for i in range(1, n):
            ans += max(nums[i] - nums[i-1], 0)
        return ans