class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        f={1:0}
        def getf(x):
            if x in f:
                return f[x]
            f[x]=(getf(3*x+1) if x%2==1 else getf(x//2))+1
            return f[x]
        l=list(range(lo,hi+1))
        l.sort(key=lambda x:(getf(x),x))
        return l[k-1]

                