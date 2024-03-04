class Solution:
    def pivotInteger(self, n: int) -> int:
        k=int(math.sqrt((n**2+n)//2))
        if k**2==(n**2+n)//2:
            return k
        return -1