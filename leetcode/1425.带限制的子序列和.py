#
# @lc app=leetcode.cn id=1425 lang=python3
#
# [1425] 带限制的子序列和
#

# @lc code=start
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque()
        f = [0] * n
        f[0] = nums[0]
        for i in range(n):
            while q and q[0] < i - k:
                q.popleft()
            if q:
                f[i] = max(nums[i], f[q[0]] + nums[i])
            while q and f[q[-1]] <= f[i]:
                q.pop()
            q.append(i)
        print(f)
        return max(f)

