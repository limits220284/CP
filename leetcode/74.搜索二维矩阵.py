class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #二分法
        m,n=len(matrix),len(matrix[0])
        l,r=0,m*n-1
        while l<=r:
            mid =(l+r)//2
            if matrix[mid//n][mid%n]==target:
                return True
            elif matrix[mid//n][mid%n]>target:
                r=mid-1
            else:
                l=mid+1
        return False