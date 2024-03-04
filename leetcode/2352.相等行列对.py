class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        cnt=0
        for i in range(n):
            ans=[]
            for j in range(n):
                ans.append(grid[j][i])
            for k in range(n):
                if grid[k]==ans:
                    cnt+=1
        return cnt