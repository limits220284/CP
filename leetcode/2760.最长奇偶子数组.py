class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        i, n = 0, len(nums)
        ans = 0
        while i < n:
            if nums[i] % 2 != 0 or nums[i] > threshold:
                i += 1
                continue
            start = i
            i += 1
            while i < n and nums[i] % 2 != nums[i-1] % 2 and nums[i] <= threshold:
                i += 1
            ans = max(ans, i - start)
        return ans