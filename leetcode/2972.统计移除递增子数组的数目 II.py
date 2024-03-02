class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < n - 1 and nums[l] < nums[l + 1]:
            l += 1
        while r > 0 and nums[r] > nums[r - 1]:
            r -= 1
        if r <= l:
            return n * (n + 1) // 2
        ans = 0
        ll, rr = 0, r
        while ll <= l and ll < rr:
            while rr < n and nums[rr] <= nums[ll]:
                rr += 1
            ans += (n - rr)
            ll += 1
        ans += l + 1
        ans += n - r
        return ans + 1