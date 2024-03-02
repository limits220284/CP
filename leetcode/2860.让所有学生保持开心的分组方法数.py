class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(n+1):
            if i == 0:
                if nums[0] > i:
                    ans += 1
            elif i == n:
                if nums[-1] < n:
                    ans += 1
            else:
                if i > nums[i-1] and i < nums[i]:
                    ans += 1
        return ans