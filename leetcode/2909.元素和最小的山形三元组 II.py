class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        mi = inf
        pre = [inf] * n
        for i in range(n):
            pre[i] = mi
            mi = min(mi, nums[i])
        mi = inf
        suf = [0] * n
        for i in range(n-1, -1, -1):
            suf[i] = mi
            mi = min(mi, nums[i])
        ans = inf
        for i in range(n):
            if pre[i] < nums[i] and nums[i] > suf[i]:
                ans = min(ans, pre[i] + nums[i] + suf[i])
        return -1 if ans == inf else ans
        
        