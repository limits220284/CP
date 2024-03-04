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
    def reachableNodes(self, n: int, edges: List[List[int]], rs: List[int]) -> int:
        uf=Unionfind(n)
        dic={}
        for x in rs:
            dic[x]=True
        for edge in edges:
            if dic.get(edge[0]) or dic.get(edge[1]):
                continue
            else:
                uf.merge(edge[0],edge[1])
        res=uf.find(0)
        cnt=1
        for i in range(1,n):
            if uf.find(i)==res:
                cnt+=1
        return cnt