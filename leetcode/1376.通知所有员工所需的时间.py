class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # 求图的高度
        g = [[] for _ in range(n)]
        for i, x in enumerate(manager):
            if x == -1: continue
            g[x].append(i)
        def dfs(x):
            mx = 0
            for y in g[x]:
                mx = max(mx, dfs(y))
            return mx + informTime[x]
        return dfs(headID)
