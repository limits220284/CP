class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        a,b=0,n-1
        while a<m and b>=0:
            if matrix[a][b]==target:
                return True
            elif matrix[a][b]<target:
                a+=1
            else:
                b-=1
        return False