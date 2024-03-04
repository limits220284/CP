class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # 原地hash
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1