#
# @lc app=leetcode.cn id=1537 lang=python3
#
# [1537] 最大得分
#

# @lc code=start
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(nums1), len(nums2)
        l, r = 0, 0
        pre = 0
        ltot, rtot = 0, 0
        f, fp = 0, 0
        while l < m and r < n:
            if nums1[l] == nums2[r]:
                f = max(fp + ltot, fp + rtot) + nums1[l]
                fp = f
                ltot, rtot = 0, 0
                l += 1
                r += 1
                print(f)
            elif nums1[l] < nums2[r]:
                ltot += nums1[l]
                l += 1
            else:
                rtot += nums2[r]
                r += 1

        while l < m:
            ltot += nums1[l]
            l += 1
        while r < n:
            rtot += nums2[r]
            r += 1
        f = max(fp + ltot, fp + rtot)
        return f % MOD
                        
                
            

