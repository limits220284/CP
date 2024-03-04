class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # 思路
        # 1、找到不同的连通块
        # 2、对于连通块的每一个点都跑一遍bfs,目的是计算最大分组
        # 3、可以采用判断二分图的方式来进行优化
        # 建图
        g=[[] for i in range(n)]
        for x,y in edges:
            x-=1
            y-=1
            g[x].append(y)
            g[y].append(x)
        # bfs()
        def bfs(start):
            nonlocal n
            mx=0
            vis=[False]*n
            q=deque([start])
            cnt=0
            vis[start]=True
            while q:
                m=len(q)
                cnt+=1
                mx=max(mx,cnt)
                for i in range(m):
                    x=q.popleft()
                    for y in g[x]:
                        if not vis[y]:
                            q.append(y)
                            vis[y]=True
            return mx
        
        # 判断二分图+获取当前连通块的点集
        def dfs(x,c):
            nodes.append(x)
            color[x]=c
            for y in g[x]:
                if color[y]==c or not color[y] and not dfs(y,3-c):
                    return False
            return True
            
        color=[0]*n
        res=0
        for i,c in enumerate(color):
            ans=0
            if c: continue
            nodes=[]
            # 如果不是二分图就直接返回-1
            if not dfs(i,1):
                return -1
            for x in nodes:
                ans=max(ans,bfs(x))
            res+=ans
        return res