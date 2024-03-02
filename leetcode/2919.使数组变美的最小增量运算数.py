class Solution:
    def minIncrementOperations1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = max(k - nums[0],0)
        dp[1][1] = min(dp[0][1], dp[0][0]) + max(k - nums[1], 0)
        for i in range(2, n):
            dp[i][1] = min(dp[i-1][0], dp[i-1][1], dp[i-2][1]) + max(k - nums[i], 0)
            dp[i][0] = min(dp[i-1][1], dp[i-2][1])
        return min(dp[-1])
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @cache
        def dfs(i, j):
            if i < 0:
                return 0
            res = dfs(i - 1, 0) + max(k - nums[i], 0)
            if j < 2:
                res = min(res, dfs(i - 1, j + 1))
            return res
        return dfs(n - 1, 0)