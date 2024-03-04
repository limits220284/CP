class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n//2):
            for j in range(i,n-i-1):
                t=matrix[n-j-1][i]
                matrix[n-j-1][i]=matrix[n-i-1][n-1-j]
                matrix[n-i-1][n-1-j]=matrix[j][n-i-1]
                matrix[j][n-i-1]=matrix[i][j]
                matrix[i][j]=t