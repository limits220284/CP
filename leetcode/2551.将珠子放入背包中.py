class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        a=[]
        n=len(weights)
        for x,y in pairwise(weights):
            a.append(x+y)
        a.sort()
        return sum(a[n-k:])-sum(a[:k-1])