class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 2)
        for i in range(2, n + 2):
            f[i] = max(f[i - 1], f[i - 2] + nums[i - 2])
        return f[-1]