class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        # bfs 确定最短的环
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        def bfs(st):
            ans = inf
            dis = [-1] * n
            q = deque([(st, -1)])
            dis[st] = 0
            while q:
                ## 取出当前点
                x, fa = q.popleft()
                for y in g[x]:
                    ## 与当前点相连的点 1、没有被访问过, 距离等于dis[x] + 1 2、访问过了,而且不是父节点,代表bfs找到了一个环
                    if dis[y] < 0:
                        dis[y] = dis[x] + 1
                        q.append((y, x))
                    elif y != fa:
                        ans = min(ans, dis[x] + dis[y] + 1)
            return ans
        ans = min(bfs(x) for x in range(n))
        return ans if ans < inf else -1