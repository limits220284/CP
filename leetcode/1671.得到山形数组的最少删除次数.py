class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # 求左右两边的最长上升子序列
        n = len(nums)
        dp1 = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp1[i] = max(dp1[i], dp1[j] + 1)
        dp2 = [1] * n
        for i in range(n-1, -1, -1):
            for j in range(n-1, i-1, -1):
                if nums[i] > nums[j]:
                    dp2[i] = max(dp2[i], dp2[j] + 1)
        # 枚举顶点
        ans = 0
        for i in range(n):
            if dp1[i] > 1 and dp2[i] > 1:
                ans = max(ans, dp1[i] + dp2[i] - 1)
        return n - ans