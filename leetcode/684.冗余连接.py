class Unionfind:
    def __init__(self,n):
        self.parent=list(range(n+1))
        self.rank=[0]*(n+1)
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def merge(self,x,y):
        x,y=self.parent[x],self.parent[y]
        if x==y:
            return
        elif self.rank[x]>self.rank[y]:
            self.parent[y]=x
        elif self.rank[x]<self.rank[y]:
            self.parent[x]=y
        else:
            self.parent[y]=x
            self.rank[x]+=1
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf=Unionfind(len(edges))
        res=[]
        for edge in edges:
            if uf.find(edge[0])!=uf.find(edge[1]):
                uf.merge(edge[0],edge[1])
            else:
                return edge
        return res
            