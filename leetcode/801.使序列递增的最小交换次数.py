 #
# @lc app=leetcode.cn id=801 lang=python3
#
# [801] 使序列递增的最小交换次数
#

# @lc code=start
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        f = [[inf, inf] for _ in range(n)]
        f[0][0] = 0
        f[0][1] = 1
        for i in range(1, n):
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                f[i][0] = min(f[i][0], f[i-1][0])
                f[i][1] = min(f[i][1], f[i-1][1] + 1)
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                f[i][0] = min(f[i][0], f[i-1][1])
                f[i][1] = min(f[i][1], f[i-1][0] + 1)
        return min(f[-1])
