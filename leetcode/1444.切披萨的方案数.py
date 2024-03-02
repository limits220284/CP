#
# @lc app=leetcode.cn id=1444 lang=python3
#
# [1444] 切披萨的方案数
#

# @lc code=start
    # def ways1(self, pizza: List[str], mx: int) -> int:
    #     MOD = 10 ** 9 + 7
    #     # 首先要确定怎么切，如果是横着切，上面的没了，剩下的就是下面的披萨，方案数就是切下面披萨的方案数
    #     # 如果是竖着切，那么左边的没了，剩下的就是右边的披萨，方案数就是切右边披萨的方案数
    #     # f[i][j]代表以i, j为顶点的披萨的方案数
    #     # 采用二维前缀和进行优化
    #     # 二维前缀和进行预处理
    #     m, n = len(pizza), len(pizza[0])
    #     pre = [[0] * (n + 1) for _ in range(m + 1)]
    #     for i in range(m):
    #         for j in range(n):
    #             pre[i + 1][j + 1] = pre[i + 1][j] + pre[i][j + 1] - pre[i][j] + (1 if pizza[i][j] == 'A' else 0)
    #     def check(x1, y1, x2, y2):
    #         return pre[x2 + 1][y2 + 1] - pre[x2 + 1][y1] - pre[x1][y2 + 1] + pre[x1][y1]
    #     @cache
    #     def dfs(i, j, cnt):
    #         # 如果该顶点后面的pizza的苹果数目为1，代表无法再次切分，直接返回1
    #         if cnt == 0:
    #             if check(i, j, m - 1, n - 1):
    #                 return 1
    #             return 0
    #         res = 0
    #         # 横着切
    #         for k in range(i + 1, m):
    #             if check(i, j, k - 1, n - 1) and check(k, j, m - 1, n - 1):
    #                 res = (res + dfs(k, j, cnt - 1)) % MOD
    #         # 竖着切
    #         for k in range(j + 1, n):
    #             if check(i, j, m - 1, k - 1) and check(i, k, m - 1, n - 1):
    #                 res = (res + dfs(i, k, cnt - 1)) % MOD
    #         return res
    #     # 最多切k-1刀
    #     return dfs(0, 0, mx - 1)


class Solution:
        
        def ways(self, pizza: List[str], mx: int) -> int:
            MOD = 10 ** 9 + 7
            m, n = len(pizza), len(pizza[0])
            preSum = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(m):
                for j in range(n):
                    preSum[i + 1][j + 1] = preSum[i + 1][j] + preSum[i][j + 1] - preSum[i][j] + (1 if pizza[i][j] == 'A' else 0)
            def check(x2, y2, x1, y1):
                return preSum[x1 + 1][y1 + 1] - preSum[x2][y1 + 1] - preSum[x1 + 1][y2] + preSum[x2][y2]
            @cache
            def dfs(x, y, cnt):
                if cnt == 0:
                    if check(x, y, m - 1, n - 1):
                        return 1
                    return 0
                res = 0
                for dx in range(x, m - 1):
                    if check(x, y, dx, n - 1):
                        res = (res + dfs(dx + 1, y, cnt - 1)) % MOD
                for dy in range(y, n - 1):
                    if check(x, y, m - 1, dy):
                        res = (res + dfs(x, dy + 1, cnt - 1)) % MOD
                return res
            return dfs(0, 0, mx - 1)
            
































