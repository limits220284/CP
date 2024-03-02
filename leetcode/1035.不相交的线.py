class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        # 最长公共子序列问题
        # f[i][j] = f[i-1][j-1] + 1 if a[i] = b[j]
        # f[i][j] = max(f[i-1][j], f[i][j-1])
        f = [[0] * (n+1) for _ in range(m+1)]
        # f[0][0]
        for i in range(1, m+1):
            for j in range(1, n+1):
                f[i][j] = max(f[i-1][j], f[i][j-1])
                if nums1[i-1] == nums2[j-1]:
                    f[i][j] = f[i-1][j-1] + 1
        return f[-1][-1]