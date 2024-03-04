class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        for i,row in enumerate(grid):
            for j,x in enumerate(row):
                if i==j or n-i-1==j:
                    if x==0:
                        return False
                elif x!=0:
                        return False
        return True