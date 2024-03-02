class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # 带有状态的bfs
        grid = [[0] * n for _ in range(m)]
        q = deque()
        inx = [0, 0, 1, -1]
        iny = [1, -1, 0, 0]
        for i, j in guards:
            grid[i][j] = -1
            for k in range(4):
                q.append((i, j, k))
        for i, j in walls:
            grid[i][j] = -2
        while q:
            x, y, k = q.popleft()
            dx, dy = x + inx[k], y + iny[k]
            if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] >= 0:
                if grid[dx][dy] & (1 << k) == 0:
                    grid[dx][dy] |= 1 << k
                    q.append((dx, dy, k))
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += 1
        return ans
        