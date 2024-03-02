class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        nums.sort()
        i = 0
        while i < n:
            ans.append(nums[i + 1])
            ans.append(nums[i])
            i += 2
        return ans
        