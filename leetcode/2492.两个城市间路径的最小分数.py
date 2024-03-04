class DSU:
    def __init__(self,n):
        self.parent=(list(range(n+1)))
        self.rank=[0]*(n+1)

    def find(self,x):
        if x==self.parent[x]:
            return x
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def Union(self,x,y):
        x,y=self.find(x),self.find(y)
        if x==y:
            return
        if self.rank[x]>self.rank[y]:
            self.parent[y]=x
        elif self.rank[x]<self.rank[y]:
            self.parent[x]=y
        else:
            self.parent[x]=y
            self.rank[y]+=1    
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # 先用并查集将1和n所在的连通图找到，然后再遍历一次这个边数组，找到最小的边即可
        uf=DSU(n)
        for x,y,c in roads:
            uf.Union(x,y)
        res=100000
        # print(uf.parent)
        for x,y,c in roads:
            if uf.find(1)==uf.find(x):
                res=min(res,c)
        return res
        
        
        
        
        
        
        