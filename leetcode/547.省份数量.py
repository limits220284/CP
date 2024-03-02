class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 找到最大连通块的数量
        n = len(isConnected)
        vis = [False] * n
        def dfs(x):
            vis[x] = True
            for i in range(n):
                if isConnected[x][i] and x != i and vis[i] == False:
                    dfs(i)
        ans = 0
        for i in range(n):
            if not vis[i]:
                ans += 1
                dfs(i)
        return ans
        
        