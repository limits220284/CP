class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        while i < n and nums[i-1] < nums[i]:
            i += 1
        if i == n:
            return 0
        if nums[0] < nums[-1]:
            return -1
        mid = i
        i += 1
        while i < n and nums[i-1] < nums[i]:
            i += 1
        if i < n:
            return -1
        return n - mid