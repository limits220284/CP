"""
动态规划

f[i][j]表示以i结尾的特殊子序列的个数
看当前的数字是什么，如果当前数字是2, 那么就可以从前面的1和2转移过来
如果当前数字是1，可以从零转移过来
如果是零，可以从零转移过来
"""
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        f = [[0, 0, 0] for _ in range(n + 1)]
        for i in range(1, n + 1):
            f[i] = f[i - 1]
            if nums[i - 1] == 0:
                f[i][0] += (f[i - 1][0] + 1) % MOD # 自己开头或者接到上一个零的结尾
            else:
                f[i][nums[i - 1]] += f[i - 1][nums[i - 1]] + f[i - 1][nums[i - 1] - 1] % MOD # 接到1的结尾或者接到2的结尾
        return f[n][2] % MOD