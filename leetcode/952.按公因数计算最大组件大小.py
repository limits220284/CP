class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def merge(self,x,y):
        x,y=self.find(x),self.find(y)
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
    def largestComponentSize(self, nums) -> int:
        uf=DSU(max(nums)+1)
        for num in nums:
            i=2
            while i*i<=num:
                if num%i==0:
                    uf.merge(num,i)
                    uf.merge(num,num//i)
                i+=1
        return max(Counter(uf.find(num) for num in nums).values())