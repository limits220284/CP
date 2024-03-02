#
# @lc app=leetcode.cn id=2488 lang=python3
#
# [2488] 统计中位数为 K 的子数组
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        idx = -1
        for i, x in enumerate(nums):
            if x == k: idx = i
        cnt = Counter({0:1})
        mx, mi = 0, 0
        for i in range(idx - 1, -1, -1):
            if nums[i] < k: mi += 1
            if nums[i] > k: mx += 1
            cnt[mi-mx] += 1
        ans = cnt[0] + cnt[-1] #代表右边为空时候，满足条件的子数组
        mx, mi = 0, 0
        for i in range(idx + 1, n):
            if nums[i] > k: mx += 1
            if nums[i] < k: mi += 1
            ans += cnt[mx - mi]
            ans += cnt[mx - mi - 1]
        return ans

