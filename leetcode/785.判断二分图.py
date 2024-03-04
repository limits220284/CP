class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color=[0]*n
        def dfs(i,c):
            color[i]=c
            for x in graph[i]:
                if color[x]==0 and dfs(x,3-c)==False:
                        return False
                elif color[x]==c:
                    return False
            return True

        for i in range(n):
            if color[i]==0 and dfs(i,1)==False:
                return False
        return True