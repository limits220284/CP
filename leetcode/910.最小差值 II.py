class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = nums[-1] - nums[0]
        for i in range(n - 1):
            rich = max(nums[-1] - k, nums[i] + k)
            poor = min(nums[i + 1] - k, nums[0] + k)
            res = min(res, rich - poor)
        return res
