class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        f = [-inf, -inf]
        f[nums[0] % 2] = nums[0]
        for i in range(1, n):
            p = nums[i] % 2
            t = max(f[p] + nums[i], f[p ^ 1] + nums[i] - x)
            f[p] = max(f[p], t)
        return max(f[0], f[1])