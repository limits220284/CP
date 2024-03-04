class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row=[0 for _ in range(m)]
        column=[0 for _ in range(n)]
        for i in range(len(indices)):
            row[indices[i][0]]+=1
            column[indices[i][1]]+=1
        row_o,row_e,col_o,col_e=0,0,0,0
        for i in range(m):
            if row[i]%2==1:
                row_o+=1
            if row[i]%2==0:
                row_e+=1
        for i in range(n):
            if column[i]%2==1:
                col_o+=1
            if column[i]%2==0:
                col_e+=1
        return row_e*col_o+row_o*col_e
                
        