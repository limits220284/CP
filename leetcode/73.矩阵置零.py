class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        row=[False for i in range(m)]
        col=[False for i in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row[i]=True
                    col[j]=True
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j]=0