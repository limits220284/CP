#
# @lc app=leetcode.cn id=1027 lang=python3
#
# [1027] 最长等差数列
#

# @lc code=start
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # 最长也不过是-500
        n = len(nums)
        diff = max(nums) - min(nums)
        ans = 0
        for d in range(-diff, diff+1):
            dic = Counter()
            for x in nums:
                dic[x] = dic[x - d] + 1
            ans = max(ans, max(dic.values()))
        return ans
        

