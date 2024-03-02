class Solution:
    # 记忆化搜索
    def maximumJumps1(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i):
            if i == 0: return 0
            res = -inf
            for j in range(i):
                if -target <= nums[j] - nums[i] <= target:
                    res = max(res, dfs(j)+1)
            return res
        ans = dfs(len(nums)-1)
        return ans if ans >= 0 else -1
    # 动态规划
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        f = [-inf] * n
        f[0] = 0
        for i in range(1, n):
            for j in range(i):
                if -target <= nums[j] - nums[i] <= target:
                    f[i] = max(f[i], f[j] + 1)
        return f[n-1] if f[n-1] != -inf else -1