class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        # bfs, 需要新增一个状态表示障碍物是否用完了
        if k >= m + n - 3: return m + n - 2
        inx = [1, -1, 0, 0]
        iny = [0, 0, 1, -1]
        if grid[0][0] == 1: k -= 1
        q = deque([(0,0,k)])
        dep = 0
        st = set([(0,0,k)])
        while q:
            tot = len(q)
            for k in range(tot):
                t = q.popleft()
                if t[0] == m-1 and t[1] == n-1:
                    return dep
                for i in range(4):
                    dx, dy = t[0] + inx[i], t[1] + iny[i]
                    if 0 <= dx < m and 0 <= dy < n:
                        if grid[dx][dy] == 0:
                            if (dx, dy, t[2]) not in st:
                                st.add((dx, dy, t[2]))
                                q.append((dx, dy, t[2]))
                        else:
                            if t[2] >= 1:
                                if (dx, dy, t[2]-1) not in st:
                                    st.add((dx, dy, t[2]-1))
                                    q.append((dx, dy, t[2]-1))
            dep += 1
        return -1