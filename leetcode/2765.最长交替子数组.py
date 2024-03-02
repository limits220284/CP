class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        ans = -1
        while i < n-1:
            if nums[i+1] - nums[i] != 1:
                i += 1
                continue
            start = i
            sign = 1
            i += 1
            while i < n and nums[i] - nums[i-1] == sign:
                sign = -sign
                i += 1
            ans = max(ans, i - start)
            i -= 1
        return ans