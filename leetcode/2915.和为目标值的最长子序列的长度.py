class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        f = [[-inf] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(target + 1):
                f[i][j] = f[i-1][j]
                if j >= nums[i-1]:
                    f[i][j] = max(f[i][j], f[i-1][j-nums[i-1]] + 1)
        return -1 if f[-1][-1] == -inf else f[-1][-1]
        