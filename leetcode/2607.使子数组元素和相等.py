"""
周期为n,而且周期为k
周期最小为gcd(n,k)
本题需要保证间隔为k的元素都要相等
"""
class DSU:
    def __init__(self,n):
        self.size=[1]*(n+1)
        self.parent=list(range(n+1))
        self.rank=[0]*(n+1)
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        x,y=self.find(x),self.find(y)
        if x==y:
            return
        if self.rank[x]<self.rank[y]:
            self.parent[x]=y
            self.size[y]+=self.size[x]
        elif self.rank[x]>self.rank[y]:
            self.parent[y]=x
            self.size[x]+=self.size[y]
        else:
            self.parent[x]=y
            self.rank[y]+=1
            self.size[y]+=self.size[x]
class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        dic = defaultdict(list)
        n = len(arr)
        uf = DSU(n)
        for i in range(n):
            uf.union(i, (i+k)%n)
        for i in range(n):
            a = uf.find(uf.parent[i])
            dic[a].append(i)
        ans = 0
        for x, b in dic.items():
            b = [arr[i] for i in b]
            b.sort()
            mid = b[len(b) // 2]
            ans += sum(abs(y - mid) for y in b)
        return ans