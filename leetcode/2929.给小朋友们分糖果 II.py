class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # 第一位小朋友最多有min(n, limit) + 1种可能
        # 第二位朋友最多有min(n - a, limit) + 1种可能
        # 第三位朋友最多有min(n - a - b, limit) + 1 种可能
        ans = 0
        for x in range(min(n, limit) + 1):
            res = n - x
            if 2 * limit < res:
                continue
            ans += min(res, limit) - max(0, res - limit) + 1
        return ans
        # 动态规划
        # 首先分给第一个小朋友x个糖，问题转换成，n-x分给两个小朋友的方案数
        # dfs(i, tot) 表示给前i个朋友总共tot个糖的方案数目
        # @cache
        # def dfs(i, tot):
        #     if i == 0:
        #         if tot == 0:
        #             return 1
        #         return 0
        #     res = 0
        #     # 看分配给第i个多少颗糖果
        #     for x in range(min(limit, tot) + 1):
        #         if (i - 1) * limit < tot - x:
        #             continue
        #         res += dfs(i - 1, tot - x)
        #     return res
        # return dfs(3, n)