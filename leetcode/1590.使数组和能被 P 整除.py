class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        tot = sum(nums) % p
        if tot == 0: return 0
        cnt = {0:0}
        ans = 1e5
        pre = 0
        for i in range(1, n+1):
            pre = (pre + nums[i-1]) % p
            k = (pre - tot) % p
            if k in cnt:
                ans = min(ans, i - cnt[k])
            cnt[pre] = i
        if ans == n or ans == 1e5:
            return -1
        return ans