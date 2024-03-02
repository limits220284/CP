"""
原问题:n种题目,组合target分的方案数
假设最后一种题目做了k道题
子问题：n-1种题目，组合target - types[n-1][1]*k 分的方案数
"""


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(types)
        # @cache
        # def dfs(i, j):
        #     if i == 0:
        #         return 1 if j == 0 else 0
        #     count, marks = types[i-1]
        #     res = 0
        #     for k in range(min(count,j // marks) + 1):
        #         res += dfs(i-1, j-marks*k)
        #     return res % MOD
        # return dfs(n,target)
        # 一比一翻译成动态规划
        # 前i种组合,恰好组成j分的方案数
        f = [[0] * (target+1) for _ in range(n+1)]
        f[0][0] = 1
        for i, (count, marks) in enumerate(types):
            for j in range(target+1):
                res = 0
                for k in range(min(count, j//marks) + 1):
                    res += f[i][j-marks*k]
                f[i+1][j] = res % MOD
        return f[n][target]