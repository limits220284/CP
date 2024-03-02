class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # 跑一遍trips，看看占比最多的点
        # 非相邻节点可以采用类似于打家劫舍的树形dp思想来解决
        # 暴力dfs计算点的权重
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        cnt = [0] * n
        def dfs(x, fa, end):
            if x == end:
                cnt[x] += 1
                return True
            for y in g[x]:
                if y != fa:
                    if dfs(y, x, end):
                        cnt[x] += 1
                        return True
            return False
        for start, end in trips:
            dfs(start, -1, end)
        # 计算出每个点的代价
        price = [price[i] * cnt[i] for i in range(n)]
        # 相邻的不能同时减半
        # 当前节点不减半，剩余的可以减半或者不减半
        # 当前的减半，剩余的只能不变
        def rob3(x, fa):
            alls = price[x]
            half = alls // 2
            for y in g[x]:
                if y != fa:
                    a, h = rob3(y, x)
                    half += a
                    alls += min(a, h)
            return alls, half
        return min(rob3(0, -1))