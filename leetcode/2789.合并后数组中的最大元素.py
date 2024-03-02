class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        # 找到连续递增的序列然后求和即可,直到没有单调递增的数
        # 倒叙遍历
        n = len(nums)
        ans = 0
        r = n-1
        tot = nums[r]
        r -= 1
        while r >= 0:
            if tot >= nums[r]:
                tot += nums[r]
            else:
                ans = max(ans, tot)
                tot = nums[r]
            r -= 1
        ans = max(ans, tot)
        return ans
            