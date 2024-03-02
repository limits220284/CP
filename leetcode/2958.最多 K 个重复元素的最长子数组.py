class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # 滑动窗口
        n = len(nums)
        l, r = 0, 0
        cnt = Counter()
        ans = 0
        while r < n:
            cnt[nums[r]] += 1
            while cnt[nums[r]] > k:
                cnt[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans