class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * n
        mx = 0
        for i in range(n):
            pre[i] = mx
            mx = max(mx, nums[i])
        mx = 0
        suf = [0] * n
        for i in range(n-1, -1, -1):
            suf[i] = mx
            mx = max(mx, nums[i])
        ans = -inf
        for i in range(1, n-1):
            ans = max(ans, (pre[i] - nums[i]) * suf[i])
        return 0 if ans < 0 else ans