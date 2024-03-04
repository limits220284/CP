class Solution:
    def __init__(self):
        self.valid=False
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(sr):
            if sr==destination:
                self.valid=True
            vis[sr]=True
            for x in graph[sr]:
                if vis[x]==False:
                    dfs(x)
                if self.valid:
                    return True
            return False
        vis=[False for i in range(n)]
        m=len(edges)
        graph=[[] for i in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        dfs(source)
        return self.valid