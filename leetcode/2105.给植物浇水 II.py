class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n=len(plants)
        l,r=0,n-1
        cnt=0
        A,B=capacityA,capacityB
        while l<r:
            if A<plants[l]:
                cnt+=1
                A=capacityA
            A-=plants[l]
            if B<plants[r]:
                cnt+=1
                B=capacityB
            B-=plants[r]
            l+=1
            r-=1
        if l==r:
            if max(A,B)<plants[l]:
                cnt+=1
        return cnt
            