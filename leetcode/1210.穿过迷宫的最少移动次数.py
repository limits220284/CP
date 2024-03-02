class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # bfs, 网络空间状态搜索
        # 怎么表示状态 (x, y, 1) 表示蛇头处于某个位置，然后处于水平还是竖直的状态
        n = len(grid)
        q = deque([(0, 1, 0)])
        step = 0
        vis = set([(0, 1, 0)])
        def check(x, y):
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                return True
            return False

        while q:
            m = len(q)
            for _ in range(m):
                x, y, f = q.popleft()
                if x == n-1 and y == n-1 and f == 0:
                    return step
                # 竖直方向
                if f == 1:
                    dx, dy = x + 1, y
                    if check(dx, dy) and (dx, dy, f) not in vis:
                        vis.add((dx, dy, f))
                        q.append((dx, dy, f))
                    dx, dy = x, y + 1
                    if check(dx, dy) and check(dx - 1, dy) and (dx, dy, f) not in vis:
                        vis.add((dx, dy, f))
                        q.append((dx, dy, f))
                    dx, dy = x - 1, y + 1
                    if check(dx, dy) and check(dx + 1, dy) and (dx, dy, 1 - f) not in vis:
                        vis.add((dx, dy, 1 - f))
                        q.append((dx, dy, 1 - f))
                # 水平方向
                else:
                    dx, dy = x, y + 1
                    if check(dx, dy) and (dx, dy, f) not in vis:
                        vis.add((dx, dy, f))
                        q.append((dx, dy, f))
                    dx, dy = x + 1, y
                    if check(dx, dy) and check(dx, dy - 1) and (dx, dy, f) not in vis:
                        vis.add((dx, dy, f))
                        q.append((dx, dy, f))
                    dx, dy = x + 1, y - 1
                    if check(dx, dy) and check(dx, dy + 1) and (dx, dy, 1 - f) not in vis:
                        vis.add((dx, dy, 1 - f))
                        q.append((dx, dy, 1 - f))
            step += 1
        return -1