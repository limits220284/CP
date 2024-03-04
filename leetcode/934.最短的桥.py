class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        raws = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(raws)]
        que_one = list()
        que_zero = list()

        def bfs(i, j):
            visited[i][j] = True
            que_one.append((i, j, 0))
            while que_one or que_zero:
                if que_one:
                    dx, dy, steps = que_one.pop(0)
                else:
                    dx, dy, steps = que_zero.pop(0)
                for x, y in ((dx - 1, dy), (dx + 1, dy), (dx, dy - 1), (dx, dy + 1)):
                    if 0 <= x < raws and 0 <= y < cols and not visited[x][y]:
                        if grid[x][y] == 1:
                            if steps > 0:
                                return steps
                            else:
                                que_one.append((x, y, 0))
                        else:
                            que_zero.append((x, y, steps + 1))
                        visited[x][y] = True

        for i in range(raws):
            for j in range(cols):
                if grid[i][j] == 1:
                    return bfs(i, j)
