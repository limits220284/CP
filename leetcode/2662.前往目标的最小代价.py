class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        points = [tuple(start)]
        for x1, y1, x2, y2, cost in specialRoads:
            points.append((x1, y1))
            points.append((x2, y2))
        points.append(tuple(target))
        points = list(set(points))
        mp = {x: i for i, x in enumerate(points)}
        n = len(points)
        g = [[inf] * n for _ in range(n)]
        for x1, y1, x2, y2, cost in specialRoads:
            idx1, idx2 = mp[(x1, y1)], mp[(x2, y2)]
            g[idx1][idx2] = min(g[idx1][idx2], cost)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                idx1, idx2 = mp[points[i]], mp[points[j]]
                g[idx1][idx2] = min(g[idx1][idx2], abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]))
        print(g)
        print(mp)
        vis = [False] * n
        dis = [inf] * n
        def dijkstra(be, ed):
            dis[be] = 0
            for i in range(n):
                t = -1
                for j in range(n):
                    if not vis[j] and (t == -1 or dis[t] > dis[j]):
                        t = j
                vis[t] = True
                for k in range(n):
                    dis[k] = min(dis[k], dis[t] + g[t][k])
            return dis[ed]
        begin, end = mp[tuple(start)], mp[tuple(target)]
        k = dijkstra(begin, end)
        return k
