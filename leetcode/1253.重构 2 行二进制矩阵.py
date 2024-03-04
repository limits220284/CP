class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper+lower!=sum(colsum):
            return []
        n=len(colsum)
        res=[[0 for i in range(n)] for j in range(2)]
        cnt=sum(i==2 for i in colsum)
        if cnt>upper or cnt>lower:
            return []
        cnt=upper-cnt
        for i in range(n):
            if colsum[i]==0:
                continue
            elif colsum[i]==2:
                res[0][i]=res[1][i]=1
            elif cnt!=0:
                res[0][i]=1
                cnt-=1
            else:
                res[1][i]=1
        return res
                