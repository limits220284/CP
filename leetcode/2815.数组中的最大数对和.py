class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        for i in range(n):
            for j in range(i + 1, n):
                a = max(list(str(nums[i])))
                b = max(list(str(nums[j])))
                if a == b:
                    ans = max(ans, nums[i] + nums[j])
        return ans