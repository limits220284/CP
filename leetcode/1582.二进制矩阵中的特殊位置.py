class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0])
        row=[sum(x) for x in mat]
        col=[sum(x) for x in zip(*mat)]
        cnt=0
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1 and row[i]==1 and col[j]==1:
                    cnt+=1
        return cnt