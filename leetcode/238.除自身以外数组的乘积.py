class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, suf = [1] * (n + 1), [1] * (n + 1)
        for i in range(n):
            pre[i] = pre[i-1] * nums[i]
        for i in range(n-1, -1, -1):
            suf[i] = suf[i+1] * nums[i]
        ans = [0] * n
        for i in range(n):
            ans[i] = pre[i-1] * suf[i+1]
        return ans