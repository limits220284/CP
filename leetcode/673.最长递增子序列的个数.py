#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # 定义以f[i]为结尾的最长递增子序列的个数
        # f[i] = f[i]
        n = len(nums)
        f = [[1, 1] for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if f[j][0] >= f[i][0]:
                        f[i][0] = f[j][0] + 1
                        f[i][1] = f[j][1]
                    elif f[j][0] == f[i][0] - 1:
                        f[i][1] += f[j][1]
        mx = max([x[0] for x in f])
        ans = 0
        for x in f:
            if x[0] == mx:
                ans += x[1]
        return ans if ans != 0 else n
