class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a,b = -1,-1
        vis = set()
        s = 0
        n  = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] in vis:
                    a = grid[i][j]
                else:
                    vis.add(grid[i][j])
                    s+=grid[i][j]
        b = sum([i for i in range(1,n*n+1)])-s
        return [a,b]
        