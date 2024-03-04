class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        ans = 0
        n = len(grid)
        x, y = 0, 0
        cur = 0
        while True:
            flag = False
            for dx,dy in [[x-2,y-1],[x-1,y-2],[x-2,y+1],[x-1,y+2],[x+1,y-2],[x+2,y-1],[x+1,y+2],[x+2,y+1]]:
                if dx<n and dx>=0 and dy<n and dy>=0:
                    if grid[dx][dy] == cur + 1:
                        flag = True
                        x,y = dx,dy
                        break
            if flag == False:
                break
            else:
                cur += 1
                ans += 1
        print(ans)
        return ans == n**2 - 1