class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n=len(vals)
        g=[[] for i in range(n)]
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        parent=list(range(n))
        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]
        ans=n
        size=[1]*n
        for vx,x in sorted(zip(vals,range(n))):
            px=find(x)
            for y in g[x]:
                py=find(y)
                if px==py or vals[py]>vx:
                    continue
                if vals[py]==vx:
                    ans+=size[py]*size[px]
                    size[px]+=size[py]
                parent[py]=px
        return ans