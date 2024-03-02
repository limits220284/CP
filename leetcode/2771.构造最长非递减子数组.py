class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        f = [[1] * 2 for _ in range(n)]
        ans = 1
        for i in range(1, n):
            if nums1[i] >= nums1[i-1]:
                f[i][0] = max(f[i][0], f[i-1][0] + 1)
            if nums1[i] >= nums2[i-1]:
                f[i][0] = max(f[i][0], f[i-1][1] + 1)
            if nums2[i] >= nums2[i-1]:
                f[i][1] = max(f[i][1], f[i-1][1] + 1)
            if nums2[i] >= nums1[i-1]:
                f[i][1] = max(f[i][1], f[i-1][0] + 1)
            ans = max(ans, f[i][0], f[i][1])
        return ans