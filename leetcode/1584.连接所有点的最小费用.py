class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 感觉像是最小生成树的板子题
        # 先建图,然后确定边的长度,然后套一个kruskal算法模板即可
        def mhd(x1, y1, x2, y2):
            return abs(x1 - x2) +  abs(y1 - y2)
        def prim(be):
            res=0
            dis[be]=0
            for i in range(n):
                t=-1
                # 选取到已经加入集合中的点的最小的边
                for j in range(n):
                    if not vis[j] and (t == -1 or dis[t] > dis[j]):
                        t=j
                vis[t] = True
                if dis[t] == mx:
                    return mx
                res += dis[t]
                # 通过这个点来更新剩下的边到集合的距离
                for k in range(n):
                    dis[k] = min(dis[k], g[t][k])
            return res
        mx=float('inf')
        n = len(points)
        g=[[mx] * n for i in range(n)]
        vis=[False] * n
        dis=[mx] * n
        for i in range(n):
            for j in range(i + 1, n):
                d = mhd(points[i][0],points[i][1],points[j][0],points[j][1])
                g[i][j] = g[j][i] = d
        # print(g)
        return prim(0)

            