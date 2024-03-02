class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # 状态转移方程为:dp[j][i] = max(dp[k][j]+1,3)
        dic = {x : i for i, x in enumerate(arr)}
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        ans = 0
        for i, x in enumerate(arr):
            for j in range(i-1, -1, -1):
                if arr[j] * 2 <= x:
                    break
                if x - arr[j] in dic:
                    k = dic[x-arr[j]]
                    dp[j][i] = max(dp[k][j] + 1, 3)
                ans = max(ans, dp[j][i])
        return ans